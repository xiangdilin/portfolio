"""Convex NMF (Ding, Li & Jordan): X ~ X W G^T with W, G >= 0, X of any sign."""
from __future__ import annotations

import numpy as np

from ._utils import _inv_or_pinv, gramianMatrix, negativeEntryMatrix, positiveEntryMatrix


def initialize_G_W(S):
    """Initialise (G, W) for Convex NMF from a Semi-NMF factor ``S`` of shape (k, n).

    The input ``S`` is not modified.
    """
    G = np.array(np.asarray(S, dtype=float).T)  # copy, shape (n, k)
    W = G @ _inv_or_pinv(G.T @ G)
    G = G + 0.2
    W = positiveEntryMatrix(W) + 0.2
    return G, W


def _safe(Denominator):
    return np.where(Denominator == 0, 1e-5, Denominator)


def _G_step(G, W, pos, neg):
    GWT = G @ W.T
    posW, negW = pos @ W, neg @ W
    Numerator = posW + GWT @ negW
    Denominator = negW + GWT @ posW
    return G * np.sqrt(Numerator / _safe(Denominator))


def _W_step(G, W, pos, neg):
    posG, negG = pos @ G, neg @ G
    WGT_G = (W @ G.T) @ G
    Numerator = posG + neg @ WGT_G
    Denominator = negG + pos @ WGT_G
    return W * np.sqrt(Numerator / _safe(Denominator))


def _parts(dataMatrix):
    XTX = gramianMatrix(dataMatrix)
    return positiveEntryMatrix(XTX), negativeEntryMatrix(XTX)


def updateG(G, dataMatrix, W):
    """One multiplicative update of G (returns a new array; inputs are not modified)."""
    pos, neg = _parts(dataMatrix)
    return _G_step(G, W, pos, neg)


def updateW(G, dataMatrix, W):
    """One multiplicative update of W (returns a new array; inputs are not modified)."""
    pos, neg = _parts(dataMatrix)
    return _W_step(G, W, pos, neg)


def _rel_change(new, old):
    return np.linalg.norm(new - old) / max(np.linalg.norm(old), 1e-12)


def _convex_iterations(base, G, W, max_iter, tol):
    """Alternate G and W updates; ``base`` is the matrix whose Gramian is factorised."""
    pos, neg = _parts(base)  # computed once, not every iteration
    for _ in range(max_iter):
        G_new = _G_step(G, W, pos, neg)
        W_new = _W_step(G_new, W, pos, neg)
        done = tol is not None and max(_rel_change(G_new, G), _rel_change(W_new, W)) < tol
        G, W = G_new, W_new
        if done:
            break
    return G, W


def ConvexNMF(dataMatrix, S, max_iter, tol=None):
    """Convex NMF.

    Parameters
    ----------
    dataMatrix : (n_samples, n_features) array, entries of any sign
    S : (k, n_samples) Semi-NMF factor used for initialisation (see :func:`initialize_G_W`)
    max_iter : maximum number of iterations
    tol : if given, stop early when the relative change of G and W drops below it.
        ``None`` (default) always runs ``max_iter`` iterations, as the original code did.

    Returns
    -------
    G, W : both (n_samples, k) and non-negative
    """
    dataMatrix = np.asarray(dataMatrix, dtype=float)
    G, W = initialize_G_W(S)
    return _convex_iterations(dataMatrix.T, G, W, max_iter, tol)
