import warnings

import numpy as np
import pytest

import wssnmtf as ws

DIVISION = [[0, 29], [30, 59], [60, 89]]


def _layers(n_layers=2):
    return {i: ws.synthetic_layer(90, DIVISION, 5, random_seed=i) for i in range(n_layers)}


def _purity(true, pred):
    """Fraction of nodes whose predicted cluster's majority true label matches theirs."""
    correct = 0
    for c in np.unique(pred):
        members = true[pred == c]
        correct += np.bincount(members).max()
    return correct / len(true)


def test_recovers_planted_communities():
    A = _layers()
    H, S = ws.WSSNMTF(A, k=3, tol=1e-6, max_iter=3000, weights="all", n_init=8)
    pred = ws.actual_assignment(H)
    true = ws.expected_assignment(DIVISION)
    assert H.shape == (90, 3)
    assert set(S) == {0, 1}
    assert _purity(true, pred) >= 0.95


def test_default_weights_are_edges_and_all_is_ones():
    A = _layers(1)
    H_default, _ = ws.WSSNMTF(A, k=3, seed=3)
    H_edges, _ = ws.WSSNMTF(A, k=3, seed=3, weights="edges")
    np.testing.assert_array_equal(H_default, H_edges)
    H_all, _ = ws.WSSNMTF(A, k=3, seed=3, weights="all")
    H_custom, _ = ws.WSSNMTF(A, k=3, seed=3, weights=[np.ones((90, 90))])
    np.testing.assert_allclose(H_all, H_custom)
    with pytest.raises(ValueError):
        ws.WSSNMTF(A, k=3, weights="bogus")


def test_n_init_never_worse_than_single_run():
    A = _layers()
    W = {i: np.ones((90, 90)) for i in A}
    H1, S1 = ws.WSSNMTF(A, k=3, seed=0, weights="all", n_init=1)
    H5, S5 = ws.WSSNMTF(A, k=3, seed=0, weights="all", n_init=5)
    assert ws.reconstruction_error(A, W, H5, S5) <= ws.reconstruction_error(A, W, H1, S1) + 1e-9


def test_accepts_list_dict_and_single_matrix():
    A = _layers(1)
    H1, _ = ws.WSSNMTF(A, k=3)
    H2, _ = ws.WSSNMTF([A[0]], k=3)
    H3, _ = ws.WSSNMTF(A[0], k=3)
    np.testing.assert_allclose(H1, H2)
    np.testing.assert_allclose(H1, H3)


def test_reproducible_with_seed():
    A = _layers()
    H1, _ = ws.WSSNMTF(A, k=3, seed=1)
    H2, _ = ws.WSSNMTF(A, k=3, seed=1)
    np.testing.assert_array_equal(H1, H2)


def test_does_not_touch_global_numpy_seed():
    np.random.seed(123)
    expected = np.random.random()
    np.random.seed(123)
    ws.WSSNMTF(_layers(), k=3)
    ws.synthetic_layer(30, [[0, 29]], 3, 0)
    assert np.random.random() == expected


def test_warns_when_not_converged():
    with pytest.warns(RuntimeWarning, match="did not converge"):
        ws.WSSNMTF(_layers(), k=3, tol=0.0, max_iter=5)


def test_no_nan_on_isolated_nodes():
    A = _layers(1)
    A[0][0, :] = 0
    A[0][:, 0] = 0
    H, S = ws.WSSNMTF(A, k=3)
    assert np.all(np.isfinite(H)) and np.all(np.isfinite(S[0]))


def test_input_validation():
    with pytest.raises(ValueError):
        ws.WSSNMTF(np.ones((3, 4)), k=2)
    with pytest.raises(ValueError):
        ws.WSSNMTF(-np.ones((4, 4)), k=2)
    with pytest.raises(ValueError):
        ws.WSSNMTF(np.ones((4, 4)), k=10)


def test_weight_matrix_is_binary():
    A = _layers(1)
    W = ws.get_W(A)[0]
    np.testing.assert_array_equal(W, (A[0] > 0).astype(float))


def test_normalize_H_rows_sum_to_one():
    H = np.array([[1.0, 3.0], [0.0, 0.0], [2.0, 2.0]])
    N = ws.normalize_H(H)
    np.testing.assert_allclose(N.sum(axis=1), [1, 0, 1])


def test_expected_assignment():
    np.testing.assert_array_equal(ws.expected_assignment([[0, 1], [2, 4]]), [0, 0, 1, 1, 1])


def _simrank_reference(matrix, damping, max_iter=100, tol=1e-4):
    """Straight port of the original loop implementation."""
    n = len(matrix)
    sim = np.identity(n)
    for _ in range(max_iter):
        prev = sim.copy()
        for i in range(n):
            for j in range(n):
                Ni = ws.identify_neighbors(matrix, i)
                Nj = ws.identify_neighbors(matrix, j)
                if len(Ni) and len(Nj):
                    sim[i][j] = damping / (len(Ni) * len(Nj)) * sum(prev[a][b] for a in Ni for b in Nj)
        if np.allclose(sim, prev, atol=tol):
            break
    return sim


def test_vectorised_simrank_matches_loop_version():
    A = ws.synthetic_layer(24, [[0, 11], [12, 23]], 2, 0)
    A[5, 20] = A[20, 5] = 1
    np.testing.assert_allclose(ws.SimRank(A, 0.8), _simrank_reference(A, 0.8), atol=1e-10)


def test_new_adjacency_shape():
    A = ws.synthetic_layer(12, [[0, 5], [6, 11]], 2, 0)
    assert ws.new_adjacency(A, 0.5, 0.8).shape == A.shape


def test_feature_to_adjacency():
    X = np.array([[1.0, 0], [1.0, 0], [0, 1.0], [0, 0]])
    A = ws.feature_to_adjacency_matrix(X)
    assert np.all(np.diag(A) == 0)
    assert A[0, 1] == pytest.approx(1.0)
    assert A[0, 2] == 0
    assert np.all(A >= 0)


def test_binary_noise_density_and_symmetry():
    N = ws.binary_noise(50, 0.1, 0)
    assert np.array_equal(N, N.T)
    assert np.all(np.diag(N) == 0)
    assert N.sum() / 2 == int(0.1 * 50 * 49 / 2)


def test_synthetic_layer_properties():
    M = ws.synthetic_layer_equal_size(60, 3, 4, 0)
    assert np.array_equal(M, M.T) and np.all(np.diag(M) == 0)
    assert M.max() <= 4 and M[0, 59] == 0
    assert ws.diagonal_noise(30, [[0, 9]], 0.3).shape == (30, 30)
    assert ws.more_noise(30, (0, 4), (10, 14), 0.5, random_seed=0).shape == (30, 30)


def test_plotting_smoke():
    matplotlib = pytest.importorskip("matplotlib")
    matplotlib.use("Agg")
    pytest.importorskip("networkx")
    from wssnmtf import plotting

    A = _layers(1)[0]
    H, _ = ws.WSSNMTF(A, k=6)  # k > 4 exercises the colormap path
    plotting.plot_adjacency_matrix(A, show=False)
    plotting.graph_network(A[:20, :20], 0)
    plotting.plot_probabilities(ws.normalize_H(H), show=False)


def test_metrics_smoke():
    pytest.importorskip("sklearn")
    from wssnmtf.metrics import evaluate_clustering

    true = ws.expected_assignment(DIVISION)
    out = evaluate_clustering(true, true)
    assert out["nmi"] == pytest.approx(1.0)
