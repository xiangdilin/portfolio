"""Small matrix helpers shared by the algorithms."""
from __future__ import annotations

import numpy as np


def positiveEntryMatrix(X):
    """Positive part of a matrix X: (|X| + X) / 2."""
    return (np.abs(X) + X) / 2


def negativeEntryMatrix(X):
    """Negative part of a matrix X (returned as non-negative values): (|X| - X) / 2."""
    return (np.abs(X) - X) / 2


def gramianMatrix(X):
    """Gramian of X: X^T X."""
    return X.T @ X


def _inv_or_pinv(M):
    """Inverse of M, falling back to the pseudo-inverse if M is singular."""
    try:
        return np.linalg.inv(M)
    except np.linalg.LinAlgError:
        return np.linalg.pinv(M)
