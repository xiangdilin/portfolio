import nltk
import math
import random
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import NMF
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import polynomial_kernel, rbf_kernel, linear_kernel, pairwise_kernels


def positiveEntryMatrix(X):
    """
    Compute the positive part of a matrix X
    """
    return (np.abs(X) + X)/2


def negativeEntryMatrix(X):
    """
    Compute the negative part of a matrix X
    """
    return (np.abs(X) - X)/2


def gramianMatrix(X):
    """
    Compute the gramian of matrix X
    """
    return X.T @ X #X^TX
    
"""
========
Semi NMF
========
"""

def kmeans_cluster_indicator_matrix(dataMatrix, n_clusters):
    """
    Perform K-Means clustering on data X and create the cluster indicator matrix G.

    Parameters:
    - dataMatrix: numpy array of shape (n_samples, n_features)
    - n_clusters: number of clusters (number of topics we want for kernel SSNMF)

    Returns:
    - G: cluster indicator matrix of shape (n_samples, n_clusters)
    """
    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(dataMatrix)
    cluster_labels = kmeans.labels_

    # Create the cluster indicator matrix
    n_samples = len(cluster_labels)
    G = np.zeros((n_samples, n_clusters))
    for i, label in enumerate(cluster_labels):
        G[i, label] = 1
    return G


def initialize_G_F(dataMatrix, n_clusters):
    """
    Initialize G and F matrices for semi NMF
    Parameters:
    - dataMatrix: numpy array of shape (n_samples, n_features)
    - n_clusters: number of clusters (number of topics we want for kernel SSNMF)

    Returns: initializations of F and G
    """
    G = kmeans_cluster_indicator_matrix(dataMatrix, n_clusters)
    G += 0.2 # add 0.2 to all elements of G
    dataMatrix = dataMatrix.T
    
    GTG  = gramianMatrix(G)
    '''
    print(is_positive_semidefinite(GTG))'''
    
    determinant = np.linalg.det(GTG)
    if determinant == 0:
        F = dataMatrix @ G @ np.linalg.pinv(GTG)
    else:
        F = dataMatrix @ G @ np.linalg.inv(GTG)
    return F, G


'''def is_positive_semidefinite(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    return np.all(eigenvalues >= 0)'''


def semiNMF(dataMatrix, n_clusters, maxIters):
    """
    Perform semi NMF
    Parameters:
    - dataMatrix: numpy array of shape (n_samples, n_features)
    - n_clusters: number of clusters (number of topics we want for kernel SSNMF)
    - maxIters: max number of iterations
    Returns: updated F and G
    """
    F, G = initialize_G_F(dataMatrix, n_clusters)
    dataMatrix = dataMatrix.T
    
    for i in range(maxIters):
        GTG  = gramianMatrix(G)
        determinant = np.linalg.det(GTG)
        if determinant == 0:
            F = dataMatrix @ G @ np.linalg.pinv(GTG)
        else:
            F = dataMatrix @ G @ np.linalg.inv(GTG)
        numerator = positiveEntryMatrix(dataMatrix.T @ F) + G @ negativeEntryMatrix(gramianMatrix(F))
        denominator = negativeEntryMatrix(dataMatrix.T @ F) + G @ positiveEntryMatrix(gramianMatrix(F))
        G *= np.sqrt(numerator / denominator)
    return F, G


"""
===================
Convex Kernel SSNMF
===================
"""

def initialize_G_W(S):
    """
    Initialize matrices G and W to be used for implementing convex kernel SSNMF
    Parameters:
    - S: matrix initialized by semi-NMF
    Returns: initializations of G and W for convex kernel SSNMF
    """
    G = S.T # 140x6
    W = G @ np.linalg.inv(G.T @ G)
    G += 0.2 # 140x6
    W_pos = positiveEntryMatrix(W)
    W = W_pos + 0.2 # 140x6
    return G, W


def kernel(X, kernel_type, Y=None, **kwargs):
    """
    Compute the kernel matrix for a given kernel type.
    Parameters:
    - X: numpy array of shape (n_samples, n_features)
    - kernel_type: string, type of kernel ('linear', 'polynomial', 'rbf')
    - Y: numpy array. If Y is none, we compute the kernel matrix of X only
    - kwargs: additional parameters for kernel functions
    Returns:
    - Kernel matrix
    """
    if Y is None:
        Y = X
    if kernel_type == 'linear':
        K = linear_kernel(X, Y)
    elif kernel_type == 'polynomial':
        degree = kwargs.get('degree', 3)  # Default degree is 3
        coef0 = kwargs.get('coef0', 1)    # Default coef0 is 1
        K = polynomial_kernel(X, Y, degree=degree, coef0=coef0)
    elif kernel_type == 'rbf':
        #gamma = kwargs.get('gamma', 0.5)  # Default gamma is 0.5
        gamma = kwargs.get('gamma', 1 / X.shape[1])
        K = rbf_kernel(X, Y, gamma=gamma)
    elif kernel_type == 'sigmoid':
        gamma = kwargs.get('gamma', 0.5)  # Default gamma is 0.5
        coef0 = kwargs.get('coef0', 1)    # Default coef0 is 1
        K = pairwise_kernels(X, Y, metric='sigmoid', gamma=gamma, coef0=coef0)
    else:
        raise ValueError(f"Unsupported kernel type: {kernel_type}")
    return K


def KernelSSNMF(X, Y, lam, S, max_iter, ker, tol=1e-5):
    """
    Perform Kernel-based Semi-Supervised Nonnegative Matrix Factorization (SSNMF).

    Parameters:
    X (numpy.ndarray): Input data matrix of shape (n_samples, n_features), e.g., 140 x 1536.
    Y (numpy.ndarray): Label matrix of shape (n_samples, n_labels), e.g., 140 x 2.
    lam (float): Regularization parameter.
    S (numpy.ndarray): initialization matrix derived by semi NMF.
    max_iter (int): Maximum number of iterations.
    ker (str): Kernel type to be used in the kernel function.
    tol (float, optional): Tolerance for convergence. Default is 1e-5.

    Returns:
    tuple: Updated matrices G and W after factorization.
    """
    # X: 140 x 1536, Y: 140 x 2
    dataMatrix =  kernel(X, ker) + (lam**2) * Y @ Y.T
    A, B = semiNMF(dataMatrix, 15, 100) #new line
    
    #dataMatrix = dataMatrix.T
    G, W = initialize_G_W(B.T) #S
    for i in range(max_iter):
        G = updateG(G, dataMatrix, W)
        W = updateW(G, dataMatrix, W)
    return G, W


"""
===========================
Semi-Supervised NMF (SSNMF)
===========================
"""

def get_W(X):
    """
    Get the weight matrix where each element is 1 if the corresponding element in X is not NaN,
    and 0 if the corresponding element in X is NaN.
    Parameters:
    - X (numpy.ndarray): data matrix of shape (n_samples, n_features)
    Returns: matrix W
    """
    # Initialize the weight matrix with ones
    W = np.ones_like(X, dtype=int)
    # Set elements to 0 where the corresponding element in X is NaN
    W[np.isnan(X)] = 0
    return W

def get_L(Y):
    """
    Get the weight matrix L for labeling part. Here we used the supervised version since word embeddings have
    no missing labels. 
    Parameters:
    - Y (numpy.ndarray): data matrix of shape (n_samples, n_classes)
    Returns: matrix L
    """
    L = np.ones_like(Y, dtype=float)
    return L

def SSNMF(X, Y, r, lam, max_iter=5000):
    '''
    Perform SSNMF
    Parameters:
    - X (numpy.ndarray): data matrix of shape (n_samples, n_features)
    - Y (numpy.ndarray): data matrix of shape (n_samples, n_classes)
    - r (int): number of topics
    - lam: regularization parameter
    - max_iter: default is 5000
    Returns:
    - A: basis matrix of X
    - B: basis matrix of Y
    - S: feature matrix
    - E: list of reconstruction errors that can be used later
    '''
    np.random.seed(10)

    # define matrices and dimensions
    X = np.array(X) # n documents x m terms
    X = X.T # m x n
    Y = np.array(Y) # shape nxk, k classes (k=2)
    Y = Y.T # k x n
    m = len(X)
    n = len(X[0])
    k = len(Y)
    A = np.random.rand(m, r) # m terms x r topics
    B = np.random.rand(k, r) # k classes x r topics
    S = np.random.rand(r, n) # r topics x n documents
    W = get_W(X) # n documents x m terms
    L = get_L(Y) # shape kxn, k classes (k=2)
    E = []

    for i in range(max_iter):
        ST, AT, BT = S.T, A.T, B.T
        AS, BS = A@S, B@S
        WXST = (W*X) @ (ST)
        WAS = W*(AS)
        WASST = WAS @ ST
        A_new = A * (WXST/(WASST+1e-5)) # make sure denom is not 0
        LYST = (L*Y) @ (ST)
        LBSST = np.matmul(L*(BS), ST)
        B_new = B * LYST / (LBSST+1e-5)
        num = AT @ (W*X) + lam * BT @ (L*Y)
        denom = AT @ WAS + lam * BT @ (L*(BS))
        S_new = S * (num / (denom+1e-5))
        A, B, S = A_new, B_new, S_new
        if (i+1) % 100 == 0:
            E.append(np.linalg.norm(X - A_new @ S_new))
            #print("itr ", i+1 ,"completed")
    return A, S, B, E


"""
==========
Convex NMF
==========
"""

def updateG(G, dataMatrix, W):
    """
    Update the matrix G for convex NMF.

    Parameters:
    - G (numpy.ndarray): The matrix to be updated
    - dataMatrix (numpy.ndarray): The data matrix 
    - W (numpy.ndarray): The weight matrix

    Returns:
    numpy.ndarray: The updated matrix G.
    """
    # Compute Gramian matrix of dataMatrix
    XTX = gramianMatrix(dataMatrix) #140 x 140

    # Extract positive and negative parts of the Gramian matrix
    positiveXTX = positiveEntryMatrix(XTX) #140 x 140
    negativeXTX = negativeEntryMatrix(XTX) #140 x 140

    # Compute G multiplied by the transpose of W
    GWT = np.matmul(G, W.T) # 140 x 140

    m, n = np.shape(G)

    # Compute products
    positiveXTXW = np.matmul(positiveXTX, W)#140 x 6
    negativeXTXW = np.matmul(negativeXTX, W)#140 x 6
    rightExpressionNum = np.matmul(GWT, negativeXTXW) # 140 x 6
    rightExpressionDenom = np.matmul(GWT, positiveXTXW) # 140 x 6

    # Compute Numerator and Denominator using broadcasting
    Numerator = positiveXTXW + rightExpressionNum
    Denominator = negativeXTXW + rightExpressionDenom

    # Create a mask for zero denominator cases (before adding 1e-5)
    zero_denom_mask = Denominator == 0

    # Add a small constant to Denominator to avoid division by zero
    Denominator[zero_denom_mask] += 1e-5

    # Update G using broadcasting
    G *= np.sqrt(Numerator / Denominator)
    return G


def updateW(G, dataMatrix, W):
    """
    Update the matrix W for convex NMF.

    Parameters:
    - G (numpy.ndarray): The matrix to be used for updating W
    - dataMatrix (numpy.ndarray): The data matrix 
    - W (numpy.ndarray): The matrix to be updated

    Returns:
    numpy.ndarray: The updated matrix W
    """
    # Compute Gramian matrix of dataMatrix
    XTX = gramianMatrix(dataMatrix) #140 x 140

    # Extract positive and negative parts of the Gramian matrix
    positiveXTX = positiveEntryMatrix(XTX) #140 x 140
    negativeXTX = negativeEntryMatrix(XTX) #140 x 140

    m,n = np.shape(W)

    # Compute products
    positiveXTXG = np.matmul(positiveXTX, G) #140 x 6
    negativeXTXG = np.matmul(negativeXTX, G) #140 x 6

    # Compute W multiplied by the transpose of G
    WGT = np.matmul(W, G.T) #1536 x 140
    WGT_G = np.matmul(WGT, G) #1536 x 6

    negativeXTX_WGTG = np.matmul(negativeXTX, WGT_G) # for numerator
    positiveXTX_WGTG = np.matmul(positiveXTX, WGT_G) # for denominator

    # Compute Numerator and Denominator using broadcasting
    Numerator = positiveXTXG + negativeXTX_WGTG
    Denominator = negativeXTXG + positiveXTX_WGTG

    # Create a mask for zero denominator cases (before adding 1e-5)
    zero_denom_mask = Denominator == 0

    # Add a small constant to Denominator to avoid division by zero
    Denominator[zero_denom_mask] += 1e-5

    # Update W using broadcasting
    W *= np.sqrt(Numerator / Denominator)
    return W


def ConvexNMF(dataMatrix, S, max_iter, tol=1e-5):
    """
    Perform convex NMF
    Parameters:
    - dataMatrix (numpy.ndarray): The data matrix
    - S: feature matrix initialized by semi NMF
    - max_iter: max number of iterations
    - tol: tolerance, default is 1e-5
    Returns: updated G and W matrices
    """
    dataMatrix = dataMatrix.T
    G, W = initialize_G_W(S)

    for i in range(max_iter):
        G = updateG(G, dataMatrix, W)
        W = updateW(G, dataMatrix, W)
    return G, W


"""
======================
SVM for Classification
======================
"""

def grid_search_svm(X_train, y_train, X_test, y_test):
    """
    Perform grid search for hyperparameter tuning of an SVM model and evaluate the best model.
    
    Parameters:
    - X_train (array-like): Training features.
    - y_train (array-like): Training labels.
    - X_test (array-like): Testing features.
    - y_test (array-like): Testing labels.
    
    Returns:
    - grid_search: model found by grid search.
    """
    # Define the parameter grid
    param_grid = {
        'C': [0.1, 1, 10, 100, 1000],
        'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
        'kernel': ['rbf', 'linear', 'sigmoid', 'poly']
    }
    #, 'sigmoid', 'poly'
    # Initialize the SVC model
    svc = SVC()

    # Create a GridSearchCV object
    grid_search = GridSearchCV(estimator=svc, param_grid=param_grid, cv=5, scoring='accuracy')

    # Fit the grid search
    grid_search.fit(X_train, y_train)

    # Extract the best parameters and best score
    best_params = grid_search.best_params_
    best_score = grid_search.best_score_

    # Use the best estimator to make predictions
    best_svc = grid_search.best_estimator_
    y_pred = best_svc.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)

    # Print results
    print("Best Parameters:", best_params)
    print("Best Cross-Validation Score:", best_score)
    print("Test Accuracy:", accuracy)
    return grid_search


def best_svm(grid_search, X_train, X_test, y_train, y_test):
    """
    Parameters:
    grid_search: grid search returned by function grid_search_svm
    - X_train (array-like): Training features.
    - y_train (array-like): Training labels.
    - X_test (array-like): Testing features.
    - y_test (array-like): Testing labels.
    Return: test accuracy of the best SVM model
    """
    svm = grid_search.best_estimator_
    svm.fit(X_train, y_train)
    y_pred = svm.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred)
    y_train_pred = svm.predict(X_train)
    train_accuracy = accuracy_score(y_train, y_train_pred)
    report = classification_report(y_test, y_pred)
    
    print(f'Train Accuracy: {train_accuracy}')
    print(f"Test Accuracy: {test_accuracy}")
    #print(f"Classification Report:\n{report}")
    return test_accuracy
