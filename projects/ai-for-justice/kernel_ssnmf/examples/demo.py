"""End-to-end demo on synthetic data (no real data is used or included).

Run:  pip install -e . && python examples/demo.py
"""
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

import kernel_ssnmf as ks

# Synthetic mixed-sign "embedding-like" data with two classes
X, y = make_classification(n_samples=200, n_features=40, n_informative=10,
                           class_sep=1.5, random_state=0)
X = StandardScaler().fit_transform(X)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=0)
Y_tr = np.eye(2)[y_tr]                      # one-hot labels

baseline = SVC(kernel="rbf", C=10).fit(X_tr, y_tr).score(X_te, y_te)
print(f"SVM on raw features:            {baseline:.3f}")

# Kernel SSNMF with different kernels: fit on train, represent train and test, classify
for ker in ("linear", "polynomial", "rbf"):
    G, W = ks.KernelSSNMF(X_tr, Y_tr, lam=1, max_iter=1000, ker=ker, n_topics=6)
    Z_tr = ks.kernel_transform(X_tr, X_tr, W, ker=ker)
    Z_te = ks.kernel_transform(X_tr, X_te, W, ker=ker)
    acc = SVC(kernel="rbf", C=10).fit(Z_tr, y_tr).score(Z_te, y_te)
    print(f"Kernel SSNMF ({ker:10s}, k=6):  {acc:.3f}")

# Benchmarks from the same family
A, S, B, errors = ks.SSNMF(np.abs(X_tr), Y_tr, 6, lam=1, max_iter=500)
Z_tr = S.T
Z_te = ks.ssnmf_transform(A, np.abs(X_te)).T
acc = SVC(kernel="rbf", C=10).fit(Z_tr, y_tr).score(Z_te, y_te)
print(f"SSNMF (|X|, k=6):               {acc:.3f}")
