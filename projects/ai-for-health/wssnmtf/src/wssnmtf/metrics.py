"""Clustering accuracy metrics (require the ``metrics`` extra: scikit-learn)."""
from __future__ import annotations


def evaluate_clustering(true_labels, pred_labels, X=None) -> dict:
    """Compute external metrics (and internal ones if a data matrix ``X`` is given).

    External: homogeneity, NMI, Rand index. Internal (need ``X``, e.g. H or an
    adjacency matrix): silhouette, Calinski-Harabasz, Davies-Bouldin.
    """
    try:
        from sklearn.metrics import (
            calinski_harabasz_score, davies_bouldin_score, homogeneity_score,
            normalized_mutual_info_score, rand_score, silhouette_score,
        )
    except ImportError as e:  # pragma: no cover
        raise ImportError("Metrics need scikit-learn: install the 'metrics' extra (scikit-learn)") from e

    out = {
        "homogeneity": homogeneity_score(true_labels, pred_labels),
        "nmi": normalized_mutual_info_score(true_labels, pred_labels),
        "rand": rand_score(true_labels, pred_labels),
    }
    if X is not None:
        out["silhouette"] = silhouette_score(X, pred_labels)
        out["calinski_harabasz"] = calinski_harabasz_score(X, pred_labels)
        out["davies_bouldin"] = davies_bouldin_score(X, pred_labels)
    return out
