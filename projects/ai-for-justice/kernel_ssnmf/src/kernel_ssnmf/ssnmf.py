"""Semi-Supervised NMF (SSNMF, Lee, Yoo & Choi): X ~ A S and Y ~ B S, all non-negative."""
from __future__ import annotations

import numpy as np


def get_W(X):
    """Weight matrix: 1 where X is observed, 0 where X is NaN."""
    X = np.asarray(X, dtype=float)
    return (~np.isnan(X)).astype(int)


def get_L(Y):
    """Label weight matrix (all ones: supervised, no missing labels)."""
    return np.ones_like(np.asarray(Y), dtype=float)


def SSNMF(X, Y, r, lam, max_iter=5000, random_state=10, eps=1e-5):
    """SSNMF with multiplicative updates.

    Parameters
    ----------
    X : (n_samples, n_features) non-negative data; NaN entries are treated as missing
    Y : (n_samples, n_classes) non-negative labels (e.g. one-hot)
    r : number of topics
    lam : weight of the label term
    max_iter : number of iterations
    random_state : seed for the random initialisation (a local generator is used,
        the global NumPy random state is untouched)
    eps : added to denominators to avoid division by zero

    Returns
    -------
    A : (n_features, r) basis of X
    S : (r, n_samples) topic representation of the samples
    B : (n_classes, r) basis of Y
    E : reconstruction errors ``||W * (X - A S)||_F`` recorded every 100 iterations
        (note the return order is A, S, B, E)
    """
    rng = np.random.RandomState(random_state)

    X = np.array(X, dtype=float).T          # m features x n samples
    Y = np.array(Y, dtype=float).T          # k classes  x n samples
    if X.shape[1] != Y.shape[1]:
        raise ValueError(f"X has {X.shape[1]} samples but Y has {Y.shape[1]}.")
    m, n = X.shape
    k = Y.shape[0]
    W = get_W(X)
    L = get_L(Y)
    X = np.where(W == 1, X, 0.0)            # NaN * 0 would still be NaN

    A = rng.rand(m, r)
    B = rng.rand(k, r)
    S = rng.rand(r, n)
    E = []

    for i in range(max_iter):
        ST, AT, BT = S.T, A.T, B.T
        AS, BS = A @ S, B @ S
        WAS = W * AS
        A_new = A * (((W * X) @ ST) / (WAS @ ST + eps))
        B_new = B * ((L * Y) @ ST) / (np.matmul(L * BS, ST) + eps)
        num = AT @ (W * X) + lam * BT @ (L * Y)
        denom = AT @ WAS + lam * BT @ (L * BS)
        S_new = S * (num / (denom + eps))
        A, B, S = A_new, B_new, S_new
        if (i + 1) % 100 == 0:
            E.append(np.linalg.norm(W * (X - A @ S)))
    return A, S, B, E
