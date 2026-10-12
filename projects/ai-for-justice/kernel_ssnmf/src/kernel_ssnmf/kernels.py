"""Kernel matrices."""
from __future__ import annotations

from sklearn.metrics.pairwise import linear_kernel, pairwise_kernels, polynomial_kernel, rbf_kernel


def kernel(X, kernel_type, Y=None, **kwargs):
    """Kernel matrix between the rows of X and the rows of Y (Y = X if omitted).

    Parameters
    ----------
    X : array of shape (n_samples, n_features)
    kernel_type : ``'linear'``, ``'polynomial'``, ``'rbf'`` or ``'sigmoid'``
    Y : optional array; pass e.g. a test set to get the cross-kernel K(X_train, X_test)
    kwargs : ``degree`` (3) and ``coef0`` (1) for polynomial; ``gamma`` (1 / n_features)
        for rbf; ``gamma`` (0.5) and ``coef0`` (1) for sigmoid.
    """
    if Y is None:
        Y = X
    if kernel_type == "linear":
        return linear_kernel(X, Y)
    if kernel_type == "polynomial":
        return polynomial_kernel(X, Y, degree=kwargs.get("degree", 3), coef0=kwargs.get("coef0", 1))
    if kernel_type == "rbf":
        return rbf_kernel(X, Y, gamma=kwargs.get("gamma", 1 / X.shape[1]))
    if kernel_type == "sigmoid":
        return pairwise_kernels(X, Y, metric="sigmoid", gamma=kwargs.get("gamma", 0.5),
                                coef0=kwargs.get("coef0", 1))
    raise ValueError(f"Unsupported kernel type: {kernel_type}")
