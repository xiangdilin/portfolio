"""Representations of held-out data (test-set reconstruction).

For a factorisation ``phi(X_train) ~ phi(X_train) W G^T`` the topic representation of new
points is ``S_test = A^+ phi(X_test)`` with ``A = phi(X_train) W`` (Theorems 4-7 of the
project report). Everything is computed from kernel matrices, so ``phi`` is never formed.
"""
from __future__ import annotations

import numpy as np

from .kernels import kernel

_METHODS = ("lstsq", "thm6", "thm7")


def kernel_transform(X_train, X_test, W, G=None, ker="linear", method="lstsq", rcond=1e-4,
                     **kernel_kwargs):
    """Topic representation of ``X_test`` for Convex NMF / Kernel SSNMF.

    Parameters
    ----------
    X_train : (n_train, n_features) data used to fit the factorisation
    X_test : (n_test, n_features) new data (pass ``X_train`` to represent the training data)
    W : (n_train, k) matrix returned by :func:`KernelSSNMF` or :func:`ConvexNMF`
    G : (n_train, k) matrix from the same call; only needed for ``method="thm7"``
    ker : kernel used when fitting (``"linear"`` reproduces plain Convex NMF)
    method :
        ``"lstsq"`` (default): exact least-squares projection of ``phi(X_test)`` onto the
        columns of ``A = phi(X_train) W``, i.e. ``(W^T K W)^+ W^T K(X_train, X_test)``.
        Apply it to **both** training and test data to get a consistent pair of
        representations.
        ``"thm6"``: ``W^+ K^+ K(X_train, X_test)`` (Theorem 6 of the report).
        ``"thm7"``: ``G^T K^+ K(X_train, X_test)`` (Theorem 7); use ``G`` itself as the
        training representation, as in the report's experimental protocol.
    rcond : relative cut-off for small singular values in the pseudo-inverse of ``W^T K W``
        (``method="lstsq"`` only). It keeps the projection stable when the number of topics
        reaches the rank of the kernel matrix (e.g. a linear kernel with k >= n_features).
        ``"thm6"`` / ``"thm7"`` use the plain pseudo-inverse, as in the report.
    kernel_kwargs : the same kernel parameters (``degree``, ``coef0``, ``gamma``) used for fitting

    Returns
    -------
    (n_test, k) array with the same orientation as ``G``.
    """
    if method not in _METHODS:
        raise ValueError(f"method must be one of {_METHODS}, got {method!r}.")
    X_train = np.asarray(X_train, dtype=float)
    X_test = np.asarray(X_test, dtype=float)
    W = np.asarray(W, dtype=float)
    if W.shape[0] != X_train.shape[0]:
        raise ValueError(f"W has {W.shape[0]} rows but X_train has {X_train.shape[0]} samples.")

    K = kernel(X_train, ker, **kernel_kwargs)
    K_cross = kernel(X_train, ker, Y=X_test, **kernel_kwargs)

    if method == "lstsq":
        S_test = np.linalg.pinv(W.T @ K @ W, rcond=rcond) @ (W.T @ K_cross)
    elif method == "thm6":
        S_test = np.linalg.pinv(W) @ np.linalg.pinv(K) @ K_cross
    else:
        if G is None:
            raise ValueError('method="thm7" needs G.')
        G = np.asarray(G, dtype=float)
        S_test = G.T @ np.linalg.pinv(K) @ K_cross
    return S_test.T


def ssnmf_transform(A, X_test):
    """Topic representation of new samples for SSNMF: ``S_test = A^+ X_test^T``.

    Parameters
    ----------
    A : (n_features, r) basis returned by :func:`SSNMF`
    X_test : (n_test, n_features) new data

    Returns
    -------
    (r, n_test) array, the same orientation as the ``S`` returned by :func:`SSNMF`
    (transpose it to feed a classifier).
    """
    return np.linalg.pinv(np.asarray(A, dtype=float)) @ np.asarray(X_test, dtype=float).T
