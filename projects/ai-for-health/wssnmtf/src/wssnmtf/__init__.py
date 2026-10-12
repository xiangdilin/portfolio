"""wssnmtf: Weighted Simultaneous Symmetric NMTF for multilayer community detection."""
from .core import (
    WSSNMTF, actual_assignment, compute_Wi, expected_assignment,
    get_eta, get_H_and_S, get_W, normalize_H, reconstruction_error,
)
from .similarity import SimRank, feature_to_adjacency_matrix, identify_neighbors, new_adjacency
from .synthetic import (
    binary_noise, diagonal_noise, more_noise, synthetic_layer, synthetic_layer_equal_size,
)

__version__ = "0.1.0"

__all__ = [
    "WSSNMTF", "get_H_and_S", "get_W", "compute_Wi", "get_eta",
    "normalize_H", "reconstruction_error", "actual_assignment", "expected_assignment",
    "SimRank", "new_adjacency", "feature_to_adjacency_matrix", "identify_neighbors",
    "synthetic_layer", "synthetic_layer_equal_size", "binary_noise", "diagonal_noise", "more_noise",
    "__version__",
]
