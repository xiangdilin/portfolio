"""kernel_ssnmf: Semi-NMF, Convex NMF, SSNMF and Kernel SSNMF for mixed-sign data."""
from ._utils import gramianMatrix, negativeEntryMatrix, positiveEntryMatrix
from .convex import ConvexNMF, initialize_G_W, updateG, updateW
from .kernel_ssnmf import KernelSSNMF
from .kernels import kernel
from .seminmf import initialize_G_F, kmeans_cluster_indicator_matrix, semiNMF
from .ssnmf import SSNMF, get_L, get_W
from .svm import best_svm, grid_search_svm
from .transform import kernel_transform, ssnmf_transform

__version__ = "0.1.0"

__all__ = [
    "positiveEntryMatrix", "negativeEntryMatrix", "gramianMatrix",
    "kmeans_cluster_indicator_matrix", "initialize_G_F", "semiNMF",
    "initialize_G_W", "updateG", "updateW", "ConvexNMF",
    "kernel", "KernelSSNMF",
    "get_W", "get_L", "SSNMF",
    "grid_search_svm", "best_svm",
    "kernel_transform", "ssnmf_transform",
    "__version__",
]
