# wssnmtf

Weighted Simultaneous Symmetric Non-negative Matrix Tri-Factorization (WSSNMTF) for community detection in **multilayer networks**, optimised with multiplicative (natural-gradient) updates.

Given several adjacency matrices over the same set of nodes (weights may be non-binary), `wssnmtf` finds one **shared community indicator matrix `H`** (`n × k`) plus a `k × k` matrix `S_i` for each layer, so that `A_i ≈ H S_i Hᵀ` on the observed entries.

> Developed as part of my REU 2023 project (AI for Health). <!-- TODO: add advisor / program / funding acknowledgement if required -->
>
> Based on the algorithm in: <https://ieeexplore.ieee.org/abstract/document/7899821>
> Please cite the original paper if you use this package. <!-- TODO: add full citation / BibTeX -->

## Installation

Install directly from GitHub (the package lives in a subdirectory of my portfolio repository):

```bash
pip install "git+https://github.com/xiangdilin/portfolio.git#subdirectory=projects/ai-for-health/wssnmtf"
```

With optional extras (plotting: matplotlib + networkx; metrics: scikit-learn):

```bash
pip install "wssnmtf[plot,metrics] @ git+https://github.com/xiangdilin/portfolio.git#subdirectory=projects/ai-for-health/wssnmtf"
```

Or clone and install locally:

```bash
git clone https://github.com/xiangdilin/portfolio.git
cd portfolio/projects/ai-for-health/wssnmtf
pip install -e ".[plot,metrics]"
```

## Quick start

```python
import wssnmtf as ws

division = [[0, 49], [50, 99], [100, 149]]            # planted communities
layers = {i: ws.synthetic_layer(150, division, max_entry=5, random_seed=i) for i in range(2)}

H, S = ws.WSSNMTF(layers, k=3, tol=1e-5, max_iter=2000, weights="all", n_init=10)

labels = ws.actual_assignment(H)        # hard community label per node
probs  = ws.normalize_H(H)              # soft membership, rows sum to 1
```

Evaluate and plot (needs the `plot` and `metrics` extras):

```python
from wssnmtf.metrics import evaluate_clustering
from wssnmtf.plotting import plot_probabilities

print(evaluate_clustering(ws.expected_assignment(division), labels))
plot_probabilities(probs)
```

See [`examples/demo.py`](examples/demo.py) for a complete script.

## API overview

| Module | Contents |
| --- | --- |
| `wssnmtf` (core) | `WSSNMTF`, `get_H_and_S`, `get_W`, `normalize_H`, `actual_assignment`, `expected_assignment` |
| `wssnmtf.similarity` | `SimRank`, `new_adjacency`, `feature_to_adjacency_matrix` |
| `wssnmtf.synthetic` | `synthetic_layer`, `synthetic_layer_equal_size`, `binary_noise`, `diagonal_noise`, `more_noise` |
| `wssnmtf.plotting` | `plot_adjacency_matrix`, `graph_network`, `plot_probabilities` |
| `wssnmtf.metrics` | `evaluate_clustering` |

### `WSSNMTF(A, k, tol=1e-4, eta=1e-5, max_iter=1000, seed=42, eps=1e-10)`

| Argument | Meaning |
| --- | --- |
| `A` | dict / list of symmetric, non-negative `(n, n)` arrays (or one array) |
| `k` | number of communities |
| `tol` | stop when the change between iterations falls below this |
| `eta` | regularisation trade-off parameter (float or one per layer) |
| `max_iter` | iteration cap; a `RuntimeWarning` is raised if reached |
| `seed` | seed for the random initialisation (local RNG, global state untouched) |
| `eps` | floor for denominators to avoid division by zero |
| `weights` | `"edges"` (default): fit only entries where `A > 0`. `"all"`: fit every entry (plain symmetric NMTF). Or pass your own weight matrices |
| `n_init` | number of random restarts; the run with the lowest reconstruction error is returned |

Returns `(H, S)` where `S` is a dict `{layer_index: S_i}`.

## Notes

- **Choosing `weights`.** With the default `weights="edges"` the loss ignores non-edges, so a trivial "everything in one community" solution fits well and communities can be hard to separate on fully observed networks. Use `weights="all"` for those; keep `"edges"` when zeros mean *missing* rather than *absent*.
- **Local minima.** Multiplicative NMTF updates depend on the random initialisation. Use `n_init > 1` and check results; very unbalanced community sizes are harder.
- `SimRank` is vectorised but still builds dense `n × n` matrices; it is intended for small/medium graphs.
- Input must be non-negative. A warning is issued for asymmetric layers.

## Development

```bash
cd projects/ai-for-health/wssnmtf
pip install -e ".[dev]"
pytest
```

## License

MIT, see [LICENSE](LICENSE).
