"""Helpers for building more informative adjacency matrices."""
from __future__ import annotations

import numpy as np


def identify_neighbors(matrix: np.ndarray, node_index: int) -> np.ndarray:
    """Indices of the neighbours of ``node_index`` (itself excluded)."""
    neighbors = np.nonzero(matrix[node_index])[0]
    return neighbors[neighbors != node_index]


def SimRank(matrix: np.ndarray, damping: float, max_iter: int = 100, tol: float = 1e-4) -> np.ndarray:
    """SimRank similarity (second-order proximity), vectorised.

    Same recursion as the original loop implementation:
    s(i, j) = damping / (|N_i||N_j|) * sum_{a in N_i, b in N_j} s(a, b),
    computed for all pairs at once as ``damping * B S B^T / (d d^T)``.
    Pairs where either node has no neighbours keep their previous value.
    """
    M = np.asarray(matrix)
    n = M.shape[0]
    B = (M != 0).astype(float)
    np.fill_diagonal(B, 0.0)
    deg = B.sum(axis=1)
    valid = np.outer(deg > 0, deg > 0)
    denom = np.outer(deg, deg)
    denom[~valid] = 1.0

    sim = np.identity(n)
    for _ in range(max_iter):
        prev = sim.copy()
        sim = np.where(valid, damping * (B @ prev @ B.T) / denom, prev)
        if np.allclose(sim, prev, atol=tol):
            break
    return sim


def new_adjacency(matrix: np.ndarray, weight: float, damping: float) -> np.ndarray:
    """First-order proximity (the matrix) + ``weight`` * SimRank second-order proximity."""
    return np.asarray(matrix) + weight * SimRank(matrix, damping)


def feature_to_adjacency_matrix(feature_matrix: np.ndarray, clip_negative: bool = True) -> np.ndarray:
    """Adjacency matrix from a feature matrix via cosine similarity (diagonal set to 0).

    ``clip_negative`` sets negative similarities to 0, since WSSNMTF requires
    non-negative input.
    """
    X = np.asarray(feature_matrix, dtype=float)
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    Xn = X / norms
    sim = Xn @ Xn.T
    np.fill_diagonal(sim, 0.0)
    if clip_negative:
        sim = np.clip(sim, 0.0, None)
    return sim
