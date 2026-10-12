"""Plotting helpers (require the ``plot`` extra: matplotlib, networkx)."""
from __future__ import annotations

import numpy as np


def _plt():
    try:
        import matplotlib.pyplot as plt
    except ImportError as e:  # pragma: no cover
        raise ImportError("Plotting needs matplotlib: install the 'plot' extra (matplotlib, networkx)") from e
    return plt


def plot_adjacency_matrix(A, tick_step: int = 100, markersize: float = 0.3, show: bool = True):
    """Spy plot of the non-zero pattern of ``A``. Returns the matplotlib Axes."""
    plt = _plt()
    A = np.asarray(A)
    fig, ax = plt.subplots()
    ax.spy(A != 0, markersize=markersize)
    ax.set_xlabel("Node Index")
    ax.set_ylabel("Node Index")
    ax.set_xticks(np.arange(0, len(A) + 1, tick_step))
    ax.set_yticks(np.arange(0, len(A) + 1, tick_step))
    if show:
        plt.show()
    return ax


def graph_network(layer, i=None, ax=None):
    """Draw one layer as a network graph. Returns the matplotlib Axes."""
    plt = _plt()
    try:
        import networkx as nx
    except ImportError as e:  # pragma: no cover
        raise ImportError("graph_network needs networkx: install the 'plot' extra (matplotlib, networkx)") from e
    if ax is None:
        _, ax = plt.subplots()
    G = nx.from_numpy_array(np.asarray(layer))
    nx.draw_networkx(G, ax=ax, with_labels=False, node_size=40,
                     node_color="lightblue", edge_color="grey", width=0.02)
    if i is not None:
        ax.set_title(f"Layer {i}")
    return ax


def plot_probabilities(normalized_H, colors=None, show: bool = True):
    """Stacked bar plot of each node's membership probabilities. Returns the Axes.

    ``colors`` defaults to a matplotlib colormap, so any number of communities works.
    """
    plt = _plt()
    H = np.asarray(normalized_H)
    n, k = H.shape
    if colors is None:
        colors = ["orange", "grey", "lightblue", "lightgreen"] if k <= 4 else plt.cm.tab20(np.linspace(0, 1, k))
    fig, ax = plt.subplots()
    nodes = np.arange(n)
    bottom = np.zeros(n)
    for c in range(k):
        ax.bar(nodes, H[:, c], 1, bottom=bottom, label=f"Community {c}", color=colors[c])
        bottom += H[:, c]
    ax.set_xlabel("Node Number")
    ax.set_ylabel("Probability")
    ax.legend()
    fig.tight_layout()
    if show:
        plt.show()
    return ax
