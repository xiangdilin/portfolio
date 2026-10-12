"""Semi-NMF (Ding, Li & Jordan): X ~ F G^T with G >= 0 and F unconstrained."""
from __future__ import annotations

import numpy as np
from sklearn.cluster import KMeans

from ._utils import _inv_or_pinv, gramianMatrix, negativeEntryMatrix, positiveEntryMatrix


def kmeans_cluster_indicator_matrix(dataMatrix, n_clusters, random_state=42):
    """K-Means cluster indicator matrix G of shape (n_samples, n_clusters)."""
    labels = KMeans(n_clusters=n_clusters, random_state=random_state).fit(dataMatrix).labels_
    G = np.zeros((len(labels), n_clusters))
    G[np.arange(len(labels)), labels] = 1
    return G


def initialize_G_F(dataMatrix, n_clusters, random_state=42):
    """Initialise (F, G) for Semi-NMF from K-Means (0.2 is added to G)."""
    G = kmeans_cluster_indicator_matrix(dataMatrix, n_clusters, random_state)
    G += 0.2
    F = dataMatrix.T @ G @ _inv_or_pinv(gramianMatrix(G))
    return F, G


def semiNMF(dataMatrix, n_clusters, maxIters, random_state=42, eps=1e-12):
    """Semi-NMF with multiplicative updates.

    Parameters
    ----------
    dataMatrix : (n_samples, n_features) array, entries of any sign
    n_clusters : number of topics
    maxIters : number of iterations
    random_state : seed of the K-Means initialisation
    eps : floor for denominators

    Returns
    -------
    F : (n_features, n_clusters), G : (n_samples, n_clusters) non-negative
    """
    dataMatrix = np.asarray(dataMatrix, dtype=float)
    F, G = initialize_G_F(dataMatrix, n_clusters, random_state)
    X = dataMatrix.T
    for _ in range(maxIters):
        F = X @ G @ _inv_or_pinv(gramianMatrix(G))
        XtF = X.T @ F
        FtF = gramianMatrix(F)
        numerator = positiveEntryMatrix(XtF) + G @ negativeEntryMatrix(FtF)
        denominator = negativeEntryMatrix(XtF) + G @ positiveEntryMatrix(FtF)
        G = G * np.sqrt(numerator / np.maximum(denominator, eps))
    return F, G
