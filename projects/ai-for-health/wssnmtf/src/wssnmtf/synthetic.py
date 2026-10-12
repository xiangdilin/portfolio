"""Synthetic multilayer-network generators for testing and demos."""
from __future__ import annotations

import numpy as np


def _symmetrize(random: np.ndarray) -> np.ndarray:
    return np.triu(random) + np.triu(random, 1).T


def synthetic_layer_equal_size(dim: int, comm_num: int, max_entry: int, random_seed: int) -> np.ndarray:
    """Symmetric layer with ``comm_num`` equal-size diagonal communities.

    Entries are integers in ``[0, max_entry]``; the diagonal is zero.
    """
    rng = np.random.default_rng(random_seed)
    M = np.zeros((dim, dim))
    comm_dim = dim // comm_num
    for i in range(comm_num):
        block = rng.integers(0, max_entry + 1, size=(comm_dim, comm_dim))
        M[i * comm_dim:(i + 1) * comm_dim, i * comm_dim:(i + 1) * comm_dim] = _symmetrize(block)
    np.fill_diagonal(M, 0)
    return M


def synthetic_layer(dim: int, comm_division, max_entry: int, random_seed: int) -> np.ndarray:
    """Symmetric layer with communities given as inclusive index ranges.

    ``comm_division`` e.g. ``[[0, 99], [100, 149], [150, 299]]``.
    """
    rng = np.random.default_rng(random_seed)
    M = np.zeros((dim, dim))
    for start, end in comm_division:
        size = end - start + 1
        block = rng.integers(0, max_entry + 1, size=(size, size))
        M[start:end + 1, start:end + 1] = _symmetrize(block)
    np.fill_diagonal(M, 0)
    return M


def binary_noise(dim: int, density: float, random_seed: int) -> np.ndarray:
    """Symmetric 0/1 noise matrix; exactly ``int(density * dim * (dim-1) / 2)`` edges."""
    rng = np.random.default_rng(random_seed)
    rows, cols = np.triu_indices(dim, k=1)
    count = int(density * dim * (dim - 1) / 2)
    chosen = rng.permutation(len(rows))[:count]
    noise = np.zeros((dim, dim))
    noise[rows[chosen], cols[chosen]] = 1
    noise[cols[chosen], rows[chosen]] = 1
    return noise


def diagonal_noise(dim: int, noise_index, density: float, random_seed: int = 8) -> np.ndarray:
    """Binary noise blocks placed on the diagonal at the given inclusive index ranges."""
    noise = np.zeros((dim, dim))
    for start, end in noise_index:
        size = end + 1 - start
        noise[start:end + 1, start:end + 1] = binary_noise(size, density, random_seed)
    return noise


def more_noise(dim: int, row_range, column_range, density: float, random_seed=None) -> np.ndarray:
    """Binary noise in an arbitrary (not necessarily diagonal or symmetric) block."""
    rng = np.random.default_rng(random_seed)
    r0, r1 = row_range
    c0, c1 = column_range
    noise = np.zeros((dim, dim))
    noise[r0:r1 + 1, c0:c1 + 1] = (rng.random((r1 - r0 + 1, c1 - c0 + 1)) < density).astype(float)
    return noise
