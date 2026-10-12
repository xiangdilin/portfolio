import warnings

import numpy as np
import pytest
from sklearn.datasets import make_blobs, make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import kernel_ssnmf as ks


@pytest.fixture(scope="module")
def data():
    X, y = make_classification(n_samples=60, n_features=20, n_informative=6, random_state=1)
    X = StandardScaler().fit_transform(X)  # mixed-sign
    return X, y, np.eye(2)[y]


def test_pos_neg_parts():
    X = np.array([[1.0, -2.0], [-3.0, 4.0]])
    np.testing.assert_allclose(ks.positiveEntryMatrix(X) - ks.negativeEntryMatrix(X), X)
    assert ks.positiveEntryMatrix(X).min() >= 0 and ks.negativeEntryMatrix(X).min() >= 0
    np.testing.assert_allclose(ks.gramianMatrix(X), X.T @ X)


def test_seminmf_shapes_and_improves(data):
    X, _, _ = data
    F0, G0 = ks.initialize_G_F(X, 4)
    F, G = ks.semiNMF(X, 4, 100)
    assert F.shape == (20, 4) and G.shape == (60, 4)
    assert np.all(G >= 0)
    assert np.linalg.norm(X.T - F @ G.T) <= np.linalg.norm(X.T - F0 @ G0.T) + 1e-9


def test_initialize_G_W_does_not_mutate_input(data):
    X, _, _ = data
    _, G = ks.semiNMF(X, 4, 20)
    S = G.T.copy()
    S_before = S.copy()
    Gi, Wi = ks.initialize_G_W(S)
    np.testing.assert_array_equal(S, S_before)
    assert Gi.shape == Wi.shape == (60, 4) and Wi.min() >= 0.2


def test_convex_nmf_improves_and_is_nonnegative(data):
    X, _, _ = data
    _, G = ks.semiNMF(X, 4, 20)
    G0, W0 = ks.initialize_G_W(G.T)
    G1, W1 = ks.ConvexNMF(X, G.T, 200)
    assert G1.min() >= 0 and W1.min() >= 0
    err = lambda G_, W_: np.linalg.norm(X.T - X.T @ W_ @ G_.T)
    assert err(G1, W1) < err(G0, W0)


def test_convex_tol_stops_early_and_default_runs_full(data):
    X, _, _ = data
    _, G = ks.semiNMF(X, 4, 20)
    Gfull, _ = ks.ConvexNMF(X, G.T, 50)
    Gtol, _ = ks.ConvexNMF(X, G.T, 50, tol=1e9)  # stops after the first iteration
    Gone, _ = ks.ConvexNMF(X, G.T, 1)
    np.testing.assert_allclose(Gtol, Gone)
    assert not np.allclose(Gtol, Gfull)


def test_update_functions_do_not_mutate(data):
    X, _, _ = data
    _, S = ks.semiNMF(X, 3, 10)
    G, W = ks.initialize_G_W(S.T)
    G0, W0 = G.copy(), W.copy()
    ks.updateG(G, X.T, W)
    ks.updateW(G, X.T, W)
    np.testing.assert_array_equal(G, G0)
    np.testing.assert_array_equal(W, W0)


@pytest.mark.parametrize("ker", ["linear", "polynomial", "rbf", "sigmoid"])
def test_kernel_ssnmf_runs_for_all_kernels(data, ker):
    X, _, Y = data
    G, W = ks.KernelSSNMF(X, Y, 1.0, max_iter=50, ker=ker, n_topics=5)
    assert G.shape == W.shape == (60, 5)
    assert np.all(np.isfinite(G)) and np.all(np.isfinite(W))
    assert G.min() >= 0 and W.min() >= 0


def test_kernel_ssnmf_default_topics_is_15(data):
    X, _, Y = data
    G, _ = ks.KernelSSNMF(X, Y, 1.0, max_iter=5)
    assert G.shape[1] == 15


def test_kernel_ssnmf_S_sets_number_of_topics(data):
    X, _, Y = data
    _, Gs = ks.semiNMF(X, 4, 10)
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        G, _ = ks.KernelSSNMF(X, Y, 1.0, S=Gs.T, max_iter=3)          # (k, n) orientation
        assert G.shape[1] == 4
        G, _ = ks.KernelSSNMF(X, Y, 1.0, S=Gs, max_iter=3)            # (n, k) orientation
        assert G.shape[1] == 4
    with pytest.warns(UserWarning, match="n_topics"):
        G, _ = ks.KernelSSNMF(X, Y, 1.0, S=Gs.T, max_iter=3, n_topics=3)
    assert G.shape[1] == 3
    with pytest.raises(ValueError):
        ks.KernelSSNMF(X, Y, 1.0, S=np.ones((3, 7)), max_iter=3)


def test_kernel_ssnmf_validation(data):
    X, _, Y = data
    with pytest.raises(ValueError):
        ks.KernelSSNMF(X, Y[:10], 1.0, max_iter=2)
    with pytest.raises(ValueError):
        ks.KernelSSNMF(X, Y, 1.0, max_iter=2, n_topics=1000)


def test_kernel_ssnmf_reproducible_and_separates_classes():
    X, y = make_blobs(n_samples=60, centers=2, n_features=5, random_state=0, cluster_std=0.8)
    Y = np.eye(2)[y]
    G1, _ = ks.KernelSSNMF(X, Y, 1.0, max_iter=200, ker="rbf", n_topics=2)
    G2, _ = ks.KernelSSNMF(X, Y, 1.0, max_iter=200, ker="rbf", n_topics=2)
    np.testing.assert_array_equal(G1, G2)
    pred = G1.argmax(axis=1)
    acc = max((pred == y).mean(), (pred != y).mean())  # label permutation
    assert acc > 0.9


def test_kernel_function_and_cross_kernel():
    A = np.random.default_rng(0).normal(size=(6, 3))
    B = np.random.default_rng(1).normal(size=(4, 3))
    assert ks.kernel(A, "linear").shape == (6, 6)
    np.testing.assert_allclose(ks.kernel(A, "linear", Y=B), A @ B.T)
    assert ks.kernel(A, "polynomial", Y=B, degree=2).shape == (6, 4)
    with pytest.raises(ValueError):
        ks.kernel(A, "bogus")


def test_ssnmf_basic(data):
    X, _, Y = data
    A, S, B, E = ks.SSNMF(np.abs(X), Y, 3, 1.0, max_iter=300)
    assert A.shape == (20, 3) and S.shape == (3, 60) and B.shape == (2, 3)
    assert min(A.min(), S.min(), B.min()) >= 0
    assert len(E) == 3 and E[-1] <= E[0]


def test_ssnmf_reproducible_and_leaves_global_seed_alone(data):
    X, _, Y = data
    np.random.seed(7)
    expected = np.random.random()
    np.random.seed(7)
    a = ks.SSNMF(np.abs(X), Y, 3, 1.0, max_iter=20)
    assert np.random.random() == expected
    b = ks.SSNMF(np.abs(X), Y, 3, 1.0, max_iter=20)
    np.testing.assert_array_equal(a[0], b[0])


def test_ssnmf_handles_missing_entries(data):
    X, _, Y = data
    Xn = np.abs(X).copy()
    Xn[0, 0] = np.nan
    A, S, B, E = ks.SSNMF(Xn, Y, 3, 1.0, max_iter=100)
    assert np.all(np.isfinite(A)) and np.all(np.isfinite(S)) and np.all(np.isfinite(E))


def test_ssnmf_label_mismatch(data):
    X, _, Y = data
    with pytest.raises(ValueError):
        ks.SSNMF(np.abs(X), Y[:5], 3, 1.0, max_iter=2)


def test_get_W_get_L():
    X = np.array([[1.0, np.nan], [2.0, 3.0]])
    np.testing.assert_array_equal(ks.get_W(X), [[1, 0], [1, 1]])
    assert ks.get_L(np.zeros((2, 3))).shape == (2, 3)


def test_svm_helpers(capsys):
    X, y = make_blobs(n_samples=100, centers=2, random_state=0)
    Xtr, Xte, ytr, yte = train_test_split(X, y, random_state=0)
    grid = ks.grid_search_svm(Xtr, ytr, Xte, yte,
                              param_grid={"C": [1, 10], "kernel": ["linear", "rbf"]}, verbose=False)
    assert grid.best_score_ > 0.9
    acc = ks.best_svm(grid, Xtr, Xte, ytr, yte, verbose=False)
    assert acc > 0.9


def _pipeline(method, ker="polynomial", seed=0):
    X, y = make_classification(n_samples=200, n_features=40, n_informative=10,
                               class_sep=1.5, random_state=seed)
    X = StandardScaler().fit_transform(X)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=seed)
    G, W = ks.KernelSSNMF(Xtr, np.eye(2)[ytr], 1.0, max_iter=500, ker=ker, n_topics=6)
    from sklearn.svm import SVC
    if method == "lstsq":
        Ztr = ks.kernel_transform(Xtr, Xtr, W, ker=ker, method="lstsq")
    else:
        Ztr = G
    Zte = ks.kernel_transform(Xtr, Xte, W, G=G, ker=ker, method=method)
    assert Zte.shape == (len(Xte), 6)
    return SVC(kernel="rbf", C=10, gamma="scale").fit(Ztr, ytr).score(Zte, yte)


@pytest.mark.parametrize("method", ["lstsq", "thm6", "thm7"])
def test_kernel_transform_pipeline_polynomial(method):
    assert _pipeline(method) > 0.75


@pytest.mark.parametrize("ker", ["linear", "polynomial", "rbf"])
def test_kernel_transform_lstsq_on_separated_blobs(ker):
    from sklearn.svm import SVC
    X, y = make_blobs(n_samples=120, centers=2, n_features=8, cluster_std=1.0, random_state=3)
    X = StandardScaler().fit_transform(X)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=0)
    for k in (4, 8):  # k = 8 equals the rank of the linear kernel: needs the rcond cut-off
        G, W = ks.KernelSSNMF(Xtr, np.eye(2)[ytr], 1.0, max_iter=1000, ker=ker, n_topics=k)
        Ztr = ks.kernel_transform(Xtr, Xtr, W, ker=ker)
        Zte = ks.kernel_transform(Xtr, Xte, W, ker=ker)
        assert SVC(kernel="rbf", C=10, gamma="scale").fit(Ztr, ytr).score(Zte, yte) >= 0.9


def test_kernel_transform_lstsq_is_least_squares(data):
    X, _, Y = data
    G, W = ks.KernelSSNMF(X, Y, 1.0, max_iter=100, ker="linear", n_topics=4)
    Xte = X[:7]
    S = ks.kernel_transform(X, Xte, W, ker="linear").T          # (k, n_test)
    A = X.T @ W                                                  # linear kernel: phi = identity
    resid = np.linalg.norm(Xte.T - A @ S)
    for _ in range(5):                                           # no perturbation does better
        S2 = S + 0.05 * np.random.default_rng(0).normal(size=S.shape)
        assert resid <= np.linalg.norm(Xte.T - A @ S2) + 1e-9


def test_kernel_transform_validation(data):
    X, _, Y = data
    G, W = ks.KernelSSNMF(X, Y, 1.0, max_iter=5, n_topics=3)
    with pytest.raises(ValueError):
        ks.kernel_transform(X, X, W, method="bogus")
    with pytest.raises(ValueError):
        ks.kernel_transform(X, X, W, method="thm7")
    with pytest.raises(ValueError):
        ks.kernel_transform(X[:10], X, W)


def test_convex_nmf_transform_with_linear_kernel(data):
    X, _, _ = data
    _, Gs = ks.semiNMF(X, 4, 20)
    G, W = ks.ConvexNMF(X, Gs.T, 100)
    assert ks.kernel_transform(X, X[:5], W, G=G, ker="linear", method="thm7").shape == (5, 4)


def test_ssnmf_transform_is_least_squares(data):
    X, _, Y = data
    Xa = np.abs(X)
    A, S, B, E = ks.SSNMF(Xa, Y, 3, 1.0, max_iter=200)
    S_hat = ks.ssnmf_transform(A, Xa)
    assert S_hat.shape == S.shape
    assert np.linalg.norm(Xa.T - A @ S_hat) <= np.linalg.norm(Xa.T - A @ S) + 1e-9
