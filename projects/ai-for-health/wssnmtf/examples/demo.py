"""Minimal end-to-end demo: planted communities -> WSSNMTF -> plot + metrics.

Run:  pip install -e ".[plot,metrics]" && python examples/demo.py
"""
import wssnmtf as ws
from wssnmtf.metrics import evaluate_clustering
from wssnmtf.plotting import plot_adjacency_matrix, plot_probabilities

division = [[0, 49], [50, 99], [100, 149]]
dim = 150

# Two noisy layers that share the same community structure
layers = {}
for i in range(2):
    layers[i] = (
        ws.synthetic_layer(dim, division, max_entry=5, random_seed=i)
        + ws.binary_noise(dim, density=0.05, random_seed=100 + i)
    )

plot_adjacency_matrix(layers[0])

# weights="all": also penalise predicted edges where the layer has none.
# n_init=10: NMTF has local minima, so keep the best of 10 random restarts.
H, S = ws.WSSNMTF(layers, k=3, tol=1e-5, max_iter=2000, weights="all", n_init=10)

true = ws.expected_assignment(division)
pred = ws.actual_assignment(H)
print(evaluate_clustering(true, pred))

plot_probabilities(ws.normalize_H(H))
