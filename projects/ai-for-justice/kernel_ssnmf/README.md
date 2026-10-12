# kernel-ssnmf

Python implementations of **Semi-NMF**, **Convex NMF**, **Semi-Supervised NMF (SSNMF)** and **Convex Kernel SSNMF**, designed for data whose entries can have mixed signs (for example LLM embeddings). The package also includes the test-set reconstruction used to classify held-out data, and small SVM helpers for evaluating the resulting low-dimensional representations.

> Developed as part of the 2024 REU "AI for Justice" project.
> This package contains **algorithms only**. No project data is included, and all examples use synthetic data.

## Methods

| Method | Model | Function |
| --- | --- | --- |
| Semi-NMF | `X ≈ F Gᵀ`, `G ≥ 0`, `F` unconstrained | `semiNMF` |
| Convex NMF | `X ≈ X W Gᵀ`, `W, G ≥ 0` | `ConvexNMF` |
| SSNMF | `X ≈ A S`, `Y ≈ B S`, all non-negative | `SSNMF` |
| Convex Kernel SSNMF | Convex NMF on `K(X, X) + λ² Y Yᵀ` (kernelised, label-augmented) | `KernelSSNMF` |
| Test-set reconstruction | `S_test = A† φ(X_test)` with `A = φ(X_train) W` | `kernel_transform`, `ssnmf_transform` |

Kernels: linear, polynomial, RBF, sigmoid (`kernel`). Semi-NMF and Convex NMF follow Ding, Li & Jordan (*Convex and semi-nonnegative matrix factorizations*, IEEE TPAMI 2010); SSNMF follows Lee, Yoo & Choi (*Semi-supervised nonnegative matrix factorization*, IEEE Signal Processing Letters 2010). Kernel SSNMF and its reconstruction theory are extensions developed in the REU project (see the project report).

## Installation

Install directly from GitHub (the package lives in a subdirectory of my portfolio repository):

```bash
pip install "git+https://github.com/xiangdilin/portfolio.git#subdirectory=projects/ai-for-justice/kernel_ssnmf"
```

Or clone and install locally:

```bash
git clone https://github.com/xiangdilin/portfolio.git
cd portfolio/projects/ai-for-justice/kernel_ssnmf
pip install -e ".[dev]"
```

## Quick start

Fit Kernel SSNMF on a training set, represent held-out data, and classify with an SVM:

```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import kernel_ssnmf as ks

X, y = make_classification(n_samples=200, n_features=40, n_informative=10,
                           class_sep=1.5, random_state=0)
X = StandardScaler().fit_transform(X)                  # mixed-sign data is fine
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=0)
Y_tr = np.eye(2)[y_tr]                                 # one-hot labels

# 1. Factorise the training data (polynomial kernel, 6 topics)
G, W = ks.KernelSSNMF(X_tr, Y_tr, lam=1, max_iter=1000, ker="polynomial", n_topics=6)

# 2. Represent train and test data the same way
Z_tr = ks.kernel_transform(X_tr, X_tr, W, ker="polynomial")
Z_te = ks.kernel_transform(X_tr, X_te, W, ker="polynomial")

# 3. Classify
print(SVC(kernel="rbf", C=10).fit(Z_tr, y_tr).score(Z_te, y_te))
```

To grid-search the SVM instead, use `ks.grid_search_svm(Z_tr, y_tr, Z_te, y_te)`. See [`examples/demo.py`](examples/demo.py) for a complete script.

## API overview

| Function | Purpose |
| --- | --- |
| `semiNMF(X, n_clusters, maxIters)` | Returns `F`, `G` (K-Means initialisation) |
| `ConvexNMF(X, S, max_iter, tol=None)` | Returns `G`, `W`; `S` is a `(k, n)` Semi-NMF factor for initialisation |
| `KernelSSNMF(X, Y, lam, S=None, max_iter=1000, ker="linear", tol=None, n_topics=None, **kernel_kwargs)` | Returns `G`, `W` |
| `SSNMF(X, Y, r, lam, max_iter=5000)` | Returns `A, S, B, E` (**in this order**) |
| `kernel_transform(X_train, X_test, W, G=None, ker, method="lstsq")` | Topic representation of new data for Convex NMF / Kernel SSNMF, shape `(n_test, k)` |
| `ssnmf_transform(A, X_test)` | Topic representation of new data for SSNMF, shape `(r, n_test)` |
| `kernel(X, kernel_type, Y=None, **kw)` | Kernel matrix; pass `Y` for cross-kernels such as `K(X_train, X_test)` |
| `grid_search_svm(...)`, `best_svm(...)` | SVM grid search and accuracy reporting |
| `positiveEntryMatrix`, `negativeEntryMatrix`, `gramianMatrix` | Helpers |

### Representing held-out data

`kernel_transform` computes `S_test = A† φ(X_test)` from kernel matrices only (no explicit feature map), with `ker` and kernel parameters matching those used for fitting. Three variants are available through `method`:

| `method` | Formula | Use with |
| --- | --- | --- |
| `"lstsq"` (default) | `(Wᵀ K W)† Wᵀ K(X_train, X_test)`: exact least-squares projection onto the columns of `A = φ(X_train) W` | the same call on `X_train` for the training representation |
| `"thm6"` | `W† K† K(X_train, X_test)` (Theorem 6 of the report) | `G` as the training representation |
| `"thm7"` | `Gᵀ K† K(X_train, X_test)` (Theorem 7 of the report) | `G` as the training representation |

On synthetic data, `"lstsq"` applied to both training and test data was the most robust across kernels, while the `G`-based variants of the report worked best with the polynomial kernel. For plain Convex NMF use `ker="linear"` with the `W` (and `G`) returned by `ConvexNMF`.

## Notes and limitations

- **Number of topics in `KernelSSNMF`.** Pass `n_topics`, or pass a topic matrix `S` and its shape sets the number of topics (only the shape is used; the initial values are recomputed by Semi-NMF on the kernel matrix, as in Algorithm 3 of the report). With neither, it defaults to 15. The original script ignored `S` and always used 15 topics.
- **`tol`.** `ConvexNMF` and `KernelSSNMF` run exactly `max_iter` iterations unless you pass `tol`, which enables early stopping on the relative change of `G` and `W`.
- **Choosing `k` and the kernel.** With a linear kernel, the kernel matrix has rank at most `n_features`, so very large `k` is not meaningful. `kernel_transform` truncates tiny singular values (`rcond=1e-4`) to stay stable in that regime.
- **Reproducibility.** `semiNMF` and `KernelSSNMF` initialise with K-Means (`random_state=42`); `SSNMF` uses `random_state=10`. K-Means defaults can differ between scikit-learn versions, so exact numbers may vary across versions.
- Kernel SSNMF works with the full `n × n` kernel matrix, so memory grows quadratically with the number of samples.

## Development

```bash
cd projects/ai-for-justice/kernel_ssnmf
pip install -e ".[dev]"
pytest
```

## License

MIT, see [LICENSE](LICENSE).
