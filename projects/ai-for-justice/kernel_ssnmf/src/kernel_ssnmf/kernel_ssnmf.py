"""Convex Kernel Semi-Supervised NMF (Kernel SSNMF)."""
from __future__ import annotations

import warnings

import numpy as np

from .convex import _convex_iterations, initialize_G_W
from .kernels import kernel
from .seminmf import semiNMF


def _topics_from_S(S, n_samples):
    """Number of topics encoded in the shape of a topic matrix S, shape (k, n) or (n, k)."""
    a, b = np.asarray(S).shape
    if b == n_samples:
        return a
    if a == n_samples:
        return b
    raise ValueError(f"S has shape {(a, b)}, which does not match {n_samples} samples.")


def KernelSSNMF(X, Y, lam, S=None, max_iter=1000, ker="linear", tol=None,
                n_topics=None, semi_iters=100, random_state=42, **kernel_kwargs):
    """Kernel SSNMF: Convex NMF on ``K(X, X) + lam^2 Y Y^T`` initialised by Semi-NMF.

    Parameters
    ----------
    X : (n_samples, n_features) data matrix, entries of any sign
    Y : (n_samples, n_labels) label matrix (e.g. one-hot)
    lam : weight of the label part
    S : optional topic matrix, shape (k, n_samples). Only its shape is used, to set the
        number of topics k; the initial values are always recomputed by Semi-NMF on the
        kernel matrix (Algorithm 3 of the report). Ignored if ``n_topics`` is given.
    max_iter : number of Convex NMF iterations
    ker : ``'linear'``, ``'polynomial'``, ``'rbf'`` or ``'sigmoid'``
    tol : optional early-stopping tolerance (relative change of G and W); None = off
    n_topics : number of topics k. Default: taken from ``S`` if given, else 15
        (the value the original script hard-coded).
    semi_iters : Semi-NMF iterations used for the initialisation (original: 100)
    random_state : seed of the K-Means initialisation
    kernel_kwargs : passed to :func:`kernel_ssnmf.kernel` (``degree``, ``coef0``, ``gamma``)

    Returns
    -------
    G, W : both (n_samples, n_topics) and non-negative
    """
    X = np.asarray(X, dtype=float)
    Y = np.asarray(Y, dtype=float)
    if Y.ndim == 1:
        Y = Y.reshape(-1, 1)
    if X.shape[0] != Y.shape[0]:
        raise ValueError(f"X has {X.shape[0]} samples but Y has {Y.shape[0]}.")
    if n_topics is None:
        n_topics = _topics_from_S(S, X.shape[0]) if S is not None else 15
    elif S is not None:
        warnings.warn("Both `S` and `n_topics` were given; `n_topics` is used and `S` is ignored.",
                      UserWarning, stacklevel=2)
    if not (1 <= n_topics <= X.shape[0]):
        raise ValueError(f"n_topics must be between 1 and {X.shape[0]}, got {n_topics}.")

    dataMatrix = kernel(X, ker, **kernel_kwargs) + (lam ** 2) * Y @ Y.T
    _, B = semiNMF(dataMatrix, n_topics, semi_iters, random_state)
    G, W = initialize_G_W(B.T)
    return _convex_iterations(dataMatrix, G, W, max_iter, tol)
