# Changelog

## 0.1.0
- First packaged release (refactored from the single-file `WSSNMTF.py`).
- Added `weights` (`"edges"` = original behaviour, `"all"`) and `n_init` (random restarts) options, plus `reconstruction_error`.
- Added `max_iter`, `seed`, `eps`, `eta` parameters; warning when not converged.
- Replaced global `np.random.seed` with local `numpy.random.Generator` (results differ from the old script for the same seed).
- Fixed `binary_noise` (exact density, no diagonal/duplicate entries).
- Vectorised `compute_Wi` and `SimRank`.
- Fixed missing `cosine_similarity` import in `feature_to_adjacency_matrix`.
- `plot_probabilities` now supports any number of communities.
- Split into `core`, `similarity`, `synthetic`, `plotting`, `metrics` modules.
