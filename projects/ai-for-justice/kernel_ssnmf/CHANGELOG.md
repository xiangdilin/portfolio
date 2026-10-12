# Changelog

## 0.1.0
- First packaged release (refactored from the single-file `functions.py`); numerical results of `kernel`, `semiNMF`, `ConvexNMF`, `SSNMF` and `KernelSSNMF` match the original script.
- `KernelSSNMF`: new `n_topics`, `semi_iters`, `random_state`, `tol` and kernel keyword arguments. The number of topics now comes from `n_topics`, else from the shape of `S` (which the original code ignored), else 15 (the value the original hard-coded).
- New `kernel_transform` and `ssnmf_transform`: representation of held-out data (test-set reconstruction, Theorems 4-7 of the project report, plus an exact least-squares variant).
- `ConvexNMF` / `KernelSSNMF`: `tol` now actually enables early stopping (default `None` = run `max_iter` iterations, as before); Gramian parts are computed once instead of every iteration.
- `initialize_G_W`, `updateG`, `updateW` no longer modify their inputs in place.
- `SSNMF`: local random generator instead of global `np.random.seed` (same random stream, so same results); NaN entries in X are now handled correctly; documented return order `A, S, B, E`.
- Singular Gram matrices fall back to the pseudo-inverse; denominators are floored to avoid division by zero.
- `grid_search_svm` accepts `param_grid`, `cv`, `n_jobs`; removed redundant refit and unused code in `best_svm`.
- Removed unused imports (nltk, pandas, seaborn, matplotlib) and dataset-specific comments.
