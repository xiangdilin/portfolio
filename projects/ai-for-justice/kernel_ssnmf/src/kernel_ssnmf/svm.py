"""SVM helpers for evaluating low-dimensional representations."""
from __future__ import annotations

from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

DEFAULT_PARAM_GRID = {
    "C": [0.1, 1, 10, 100, 1000],
    "gamma": [1, 0.1, 0.01, 0.001, 0.0001],
    "kernel": ["rbf", "linear", "sigmoid", "poly"],
}


def grid_search_svm(X_train, y_train, X_test, y_test, param_grid=None, cv=5, n_jobs=None, verbose=True):
    """Grid-search an SVC on the training set and report test accuracy.

    ``param_grid`` defaults to :data:`DEFAULT_PARAM_GRID` (500 fits with ``cv=5``;
    pass a smaller grid or ``n_jobs=-1`` to speed it up). Returns the fitted
    ``GridSearchCV`` object.
    """
    grid = GridSearchCV(SVC(), DEFAULT_PARAM_GRID if param_grid is None else param_grid,
                        cv=cv, scoring="accuracy", n_jobs=n_jobs)
    grid.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, grid.best_estimator_.predict(X_test))
    if verbose:
        print("Best Parameters:", grid.best_params_)
        print("Best Cross-Validation Score:", grid.best_score_)
        print("Test Accuracy:", accuracy)
    return grid


def best_svm(grid_search, X_train, X_test, y_train, y_test, verbose=True):
    """Train/test accuracy of the best estimator found by :func:`grid_search_svm`.

    Returns the test accuracy. (Argument order matches the original ``functions.py``.)
    """
    svm = grid_search.best_estimator_  # already refit on the full training set
    test_accuracy = accuracy_score(y_test, svm.predict(X_test))
    if verbose:
        print(f"Train Accuracy: {accuracy_score(y_train, svm.predict(X_train))}")
        print(f"Test Accuracy: {test_accuracy}")
    return test_accuracy
