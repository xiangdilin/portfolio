"""Core WSSNMTF algorithm.

Weighted Simultaneous Symmetric Non-negative Matrix Tri-Factorization,
optimised with multiplicative (natural-gradient) updates. Given N symmetric
adjacency matrices A_i that share the same node set, find a common community
indicator matrix H (n x k) and per-layer matrices S_i (k x k) such that

    W_i * A_i  ~  W_i * (H S_i H^T)

Reference: https://ieeexplore.ieee.org/abstract/document/7899821
"""
from __future__ import annotations

import warnings
from typing import Dict, List, Mapping, Sequence, Union

import numpy as np

Layers = Union[Mapping[int, np.ndarray], Sequence[np.ndarray], np.ndarray]


def _as_list(A: Layers) -> List[np.ndarray]:
    """Accept a dict, list/tuple or a single 2-D array and return a list."""
    if isinstance(A, np.ndarray):
        return [A] if A.ndim == 2 else [np.asarray(a) for a in A]
    if isinstance(A, Mapping):
        return [np.asarray(A[key]) for key in sorted(A)]
    return [np.asarray(a) for a in A]


def _validate_layers(layers: List[np.ndarray]) -> None:
    if len(layers) == 0:
        raise ValueError("At least one layer is required.")
    n = layers[0].shape[0]
    for i, a in enumerate(layers):
        if a.ndim != 2 or a.shape[0] != a.shape[1]:
            raise ValueError(f"Layer {i} must be a square 2-D matrix, got shape {a.shape}.")
        if a.shape[0] != n:
            raise ValueError(f"Layer {i} has {a.shape[0]} nodes but layer 0 has {n}.")
        if np.any(a < 0):
            raise ValueError(f"Layer {i} contains negative entries; NMTF needs non-negative input.")
        if not np.allclose(a, a.T):
            warnings.warn(f"Layer {i} is not symmetric.", stacklevel=3)


def compute_Wi(Ai: np.ndarray) -> np.ndarray:
    """Binary weight matrix of one layer: 1 where Ai > 0, else 0."""
    return (np.asarray(Ai) > 0).astype(float)


def get_W(A: Layers) -> Dict[int, np.ndarray]:
    """Binary weight matrices for all layers, as ``{layer_index: W_i}``."""
    return {i: compute_Wi(a) for i, a in enumerate(_as_list(A))}


def get_eta(A: Layers, value: float = 1e-5) -> List[float]:
    """Trade-off parameter eta for every layer (default 1e-5 for all)."""
    return [value] * len(_as_list(A))


def get_H_and_S(
    A: Layers,
    W: Layers,
    eta,
    tol: float,
    k: int,
    max_iter: int = 1000,
    seed: int = 42,
    eps: float = 1e-10,
):
    """Run the multiplicative updates.

    Parameters
    ----------
    A, W : layers and their binary weight matrices (dict / list of arrays).
    eta : float or sequence of floats (one per layer).
    tol : stop when the summed Frobenius change of H and mean change of S_i < tol.
    k : number of communities.
    max_iter : hard cap on iterations (a warning is issued if it is reached).
    seed : seed for the random initialisation of H and S_i.
    eps : lower bound for denominators, avoids division by zero.

    Returns
    -------
    H : (n, k) community indicator matrix
    S : dict ``{layer_index: (k, k) matrix}``
    """
    layers = _as_list(A)
    weights = _as_list(W)
    _validate_layers(layers)
    N, n = len(layers), layers[0].shape[0]
    if len(weights) != N:
        raise ValueError("A and W must have the same number of layers.")
    if not (1 <= k <= n):
        raise ValueError(f"k must be between 1 and the number of nodes ({n}), got {k}.")
    eta_arr = np.broadcast_to(np.asarray(eta, dtype=float), (N,))

    rng = np.random.default_rng(seed)
    H = rng.random((n, k))
    S = [rng.random((k, k)) for _ in range(N)]
    WA = [w * a for w, a in zip(weights, layers)]

    converged = False
    for _ in range(max_iter):
        # --- update H ---
        num_H = np.zeros((n, k))
        denom_H = np.zeros((n, k))
        for i in range(N):
            HS = H @ S[i]
            num_H += WA[i] @ HS
            denom_H += (weights[i] * (HS @ H.T)) @ HS
        H_new = H * (num_H / np.maximum(denom_H, eps)) ** 0.25

        # --- update S_i ---
        S_new = []
        for i in range(N):
            num_S = H_new.T @ WA[i] @ H_new
            denom_S = H_new.T @ (weights[i] * (H_new @ S[i] @ H_new.T)) @ H_new + 0.5 * eta_arr[i]
            S_new.append(S[i] * (num_S / np.maximum(denom_S, eps)) ** 0.5)

        # --- convergence check (consecutive change) ---
        diff_H = np.linalg.norm(H_new - H)
        diff_S = np.mean([np.linalg.norm(s1 - s0) for s1, s0 in zip(S_new, S)])
        H, S = H_new, S_new
        if diff_H + diff_S <= tol:
            converged = True
            break

    if not converged:
        warnings.warn(
            f"WSSNMTF did not converge within max_iter={max_iter} (tol={tol}). "
            "Consider increasing max_iter or tol.",
            RuntimeWarning,
            stacklevel=2,
        )
    return H, {i: s for i, s in enumerate(S)}


def reconstruction_error(A: Layers, W: Layers, H: np.ndarray, S) -> float:
    """Weighted squared reconstruction error  sum_i || W_i * (A_i - H S_i H^T) ||_F^2."""
    layers, weights = _as_list(A), _as_list(W)
    S_list = _as_list(S)
    return float(sum(np.sum((w * (a - H @ s @ H.T)) ** 2) for a, w, s in zip(layers, weights, S_list)))


def WSSNMTF(
    A: Layers,
    k: int,
    tol: float = 1e-4,
    eta: float = 1e-5,
    max_iter: int = 1000,
    seed: int = 42,
    eps: float = 1e-10,
    weights="edges",
    n_init: int = 1,
):
    """Run WSSNMTF on a multilayer network.

    Parameters
    ----------
    A : dict / list of symmetric non-negative (n, n) adjacency matrices, or a single matrix.
    k : number of communities.
    tol, eta, max_iter, seed, eps : see :func:`get_H_and_S`.
    weights : which entries of each layer are fitted.
        ``"edges"`` (default, original behaviour): W_i = 1 where A_i > 0, so only
        observed edges are fitted and non-edges are ignored.
        ``"all"``: W_i = all ones, i.e. plain symmetric NMTF that also penalises
        edges predicted where A_i = 0 (usually separates communities much better
        on fully observed networks).
        Or pass your own dict / list of weight matrices.
    n_init : number of random restarts (seeds ``seed .. seed+n_init-1``); the run with
        the lowest reconstruction error is returned. NMTF has many local minima,
        so ``n_init > 1`` is recommended.

    Returns
    -------
    H, S : community indicator matrix and dict of per-layer S matrices.
    """
    layers = _as_list(A)
    if isinstance(weights, str):
        if weights == "edges":
            W = get_W(layers)
        elif weights == "all":
            W = {i: np.ones_like(a, dtype=float) for i, a in enumerate(layers)}
        else:
            raise ValueError("weights must be 'edges', 'all', or a collection of weight matrices.")
    else:
        W = weights
    if n_init < 1:
        raise ValueError("n_init must be >= 1.")

    eta_list = get_eta(layers, eta)
    best = None
    any_converged = False
    for r in range(n_init):
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            H, S = get_H_and_S(layers, W, eta_list, tol, k, max_iter=max_iter, seed=seed + r, eps=eps)
        did_not_converge = any(issubclass(w.category, RuntimeWarning) for w in caught)
        for w in caught:  # re-emit everything that is not the per-run convergence warning
            if not issubclass(w.category, RuntimeWarning):
                warnings.warn_explicit(w.message, w.category, w.filename, w.lineno)
        any_converged = any_converged or not did_not_converge
        err = reconstruction_error(layers, W, H, S)
        if best is None or err < best[0]:
            best = (err, H, S)
    if not any_converged:
        warnings.warn(
            f"WSSNMTF did not converge within max_iter={max_iter} (tol={tol}) in any of "
            f"{n_init} run(s). Consider increasing max_iter or tol.",
            RuntimeWarning,
            stacklevel=2,
        )
    return best[1], best[2]


def normalize_H(H: np.ndarray) -> np.ndarray:
    """Scale every row of H to sum to 1 (rows of zeros stay zero)."""
    H = np.asarray(H, dtype=float)
    row_sums = H.sum(axis=1, keepdims=True)
    row_sums = np.where(row_sums == 0, 1.0, row_sums)
    return H / row_sums


def actual_assignment(H: np.ndarray) -> np.ndarray:
    """Hard community label of each node (argmax over each row of H)."""
    return np.argmax(H, axis=1)


def expected_assignment(comm_division: Sequence[Sequence[int]]) -> np.ndarray:
    """True labels from a division such as ``[[0, 99], [100, 149], [150, 299]]``."""
    labels = []
    for i, (start, end) in enumerate(comm_division):
        labels.extend([i] * (end - start + 1))
    return np.array(labels)
