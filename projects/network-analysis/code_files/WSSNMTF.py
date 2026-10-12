import numpy as np
import os
import math
import matplotlib.pyplot as plt
import networkx as nx

# Accuracy metrics
from sklearn.metrics.cluster import homogeneity_score
from sklearn.metrics import normalized_mutual_info_score
from sklearn.metrics import rand_score
from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabasz_score
from sklearn.metrics import davies_bouldin_score

"""
==========
WSSNMTF 
==========
Weighted Simultaneous Symmetric Non-Negative Matric Tri-Factorization, optimized with natural gradient. Input a network represented by adjacency matrix (can be non-binary in this case) and output a common community indicator matrix (H) for further operation.
Community indicator matrix (H): n by k matrix, where n is the number of nodes and k is a self-chosen parameter indicating the number of communities we want to extract from the data.
Reference: https://ieeexplore.ieee.org/abstract/document/7899821

"""

def synthetic_layer_equal_size(dim, comm_num, max_entry, random_seed):
    """
    Inputs: 1. dimension (number of nodes) 
        2. max number of edges between a pair of nodes 
        3. random seed 
        4. number of communities
    Output a random symmetric adjacency matrix representing a synthetic layer of the network with: 
    1. zero diagonal 2. non-negative integer entries 3. some established communities
    """
    M = np.zeros((dim, dim))
    comm_dim = int(dim/comm_num)
    np.random.seed(random_seed)
    
    for i in range(0, comm_num):
        # Generate random matrices with integer entries
        random = np.random.randint(0, max_entry+1, (comm_dim, comm_dim))
        # Make the matrices symmetric
        comm = np.triu(random) + np.triu(random, 1).T
        # Combine the communities
        M[i*comm_dim:(i+1)*comm_dim, i*comm_dim:(i+1)*comm_dim] = comm
    
    # Set diagonal entries to zero
    np.fill_diagonal(M, 0)
    return M


def synthetic_layer(dim, comm_division, max_entry, random_seed):
    """
    Inputs: 1. dimension (number of nodes) 
        2. 2d array representing community division 
        3. max number of edges between a pair of nodes 
        4. random seed
    Output a random symmetric adjacency matrix representing a synthetic layer of the network with: 
    1. zero diagonal 2. non-negative integer entries 3. some established communities
    """
    M = np.zeros((dim, dim))
    np.random.seed(random_seed)
    
    for i in range(0, len(comm_division)):
        # Generate random matrices with integer entries
        comm_dim = comm_division[i][1]-comm_division[i][0]+1
        random = np.random.randint(0, max_entry+1, size=(comm_dim, comm_dim))
        # Make the matrices symmetric
        comm = np.triu(random) + np.triu(random, 1).T
        # Combine the communities
        M[comm_division[i][0]:comm_division[i][1]+1, comm_division[i][0]:comm_division[i][1]+1] = comm
    
    # Set diagonal entries to zero
    np.fill_diagonal(M, 0)
    return M


def binary_noise(dim, density, random_seed):
    """
    Inputs: 1. dimension (number of nodes) 2. noise density 3. random seed
    Output: a binary noise matrix with specified density
    """
    noise = np.zeros((dim, dim))
    non_zero_count = int(density*dim*(dim-1)/2)
    np.random.seed(random_seed)
    
    # Generate indices for non-zero entries
    row_indices, col_indices = np.triu_indices(dim, k=1)
    np.random.shuffle(row_indices)
    np.random.shuffle(col_indices)
    
    # Set non-zero entries symmetrically
    noise[row_indices[:non_zero_count], col_indices[:non_zero_count]] = 1
    noise[col_indices[:non_zero_count], row_indices[:non_zero_count]] = 1
    
    # Make diagonals all zeros
    np.fill_diagonal(noise, 0)
    return noise


def diagonal_noise(dim, noise_index, density):
    """
    Add noise blocks with specified indices and density in the diagonal direction (\)
    """
    noise = np.zeros((dim, dim))
    for i in range(0, len(noise_index)):
        noise_dim = noise_index[i][1]+1-noise_index[i][0]
        noise[noise_index[i][0]:noise_index[i][1]+1, noise_index[i][0]:noise_index[i][1]+1] = binary_noise(noise_dim, density, 8)
    return noise


def more_noise(dim, row_range, column_range, density):
    """
    Add more noise blocks with any specified indices (doesn't have to be diagonal) and density
    """
    noise = np.zeros((dim, dim))
    for i in range(row_range[0], row_range[1]+1):
        for j in range(column_range[0], column_range[1]+1):
            noise[i][j] = np.random.choice([0, 1], size=1, p=[1 - density, density])
    return noise


def plot_adjacency_matrix(A):
    """
    Generate a spy plot for the given adjacency matrix.
    """
    # Convert the adjacency matrix to a binary matrix where non-zero values are set to 1
    binary_matrix = np.array(A != 0, dtype=int)

    # Get the indices of non-zero elements (connections)
    rows, cols = np.nonzero(binary_matrix)

    # Plot the spy plot
    plt.figure()
    plt.spy(binary_matrix, markersize=0.3)
    plt.xlabel('Node Index')
    plt.ylabel('Node Index')
    #plt.title('Spy Plot for Adjacency Matrix')
    plt.xticks(np.arange(0, len(A)+1, 100))
    plt.yticks(np.arange(0, len(A)+1, 100))
    #plt.grid(color='gray', linestyle='-', linewidth=0.5)
    plt.show()
    
    
def graph_network(layer, i):
    """
    Plot a network graph from adjacency matrix in the form of numpy array
    """
    G = nx.from_numpy_array(layer)
    nx.draw_networkx(G, with_labels=False, node_size=40, node_color='lightblue', edge_color='grey', width=0.02)
    plt.title('Layer '+ str(i))


"""
General notations for algorithm-related functions:
    A = nxn adjacency matrix (symmetric)
    W = binary weight matrix
    H = nxk soft cluster indicator matrix (or community indicator matrix) shared across the decompositions
    S = kxk matrix for A=HS(H^T)
    N = number of layers
    k = number of communities
    eps = trade-off parameter for balancing the influence between the two terms
    tol = some tolerance
    Random seeds are set for all random initializations. 
"""

def compute_Wi(Ai):
    """
    Compute W for the ith layer
    Input: Ai = adjacency matrix for the ith layer
    Output: Wi = binary weight matrix for the ith layer
    """
    Wi = np.zeros((len(Ai), len(Ai[0])))
    for x in range(0, len(Ai)):
        for y in range(0, len(Ai)):
            if Ai[x][y] > 0:
                Wi[x][y] = 1
    return Wi


def get_W(A):
    """
    Input: A = dict of adjacency matrices for N layers
    Output: W = dict of binary weight matrices for N layers
    """
    W = dict()
    for i in range(0, len(A)):
        Wi = compute_Wi(A[i])
        W[i] = Wi
    return W


def get_eta(A):
    """
    Use 1e-5 for all temporarily
    Output: 1d array of trade-off parameters eta
    """
    eta = []
    for i in range(0, len(A)):
        eta.append(1e-5)
    return eta


def get_H_and_S(A, W, eta, tol, k):
    """
    Derive H and S
    Inputs:
        A: dict of adjacency matrices for N layers
        W: dict of weight matrices for N layers
        k: number of communities
    Outputs: 
        H: community indicator matrix computed using ith layer as initializer
        S: a dictionary of Si matrices
    """
    # Random initializations of H and S
    np.random.seed(42)
    H = np.random.random((len(A[0][0]), k))
    S = dict()
    for i in range(0, len(A)):
        S[i] = np.random.random((k,k))
    
    f_norm = 100 # Set any large number
    while (f_norm > tol):
        # Update H
        num_H = np.zeros((len(A[0][0]), k))
        denom_H = np.zeros((len(A[0][0]), k))
        for i in range(0, len(A)):
            num_H += (W[i]*A[i])@H@S[i]
            denom_H += (W[i]*(H@S[i]@H.transpose()))@H@S[i]
        H_new = H * (np.divide(num_H, denom_H)**0.25)
        
        # Update S
        S_new = dict()
        for i in range(0, len(A)):
            num_Si = H_new.transpose()@(W[i]*A[i])@H_new
            denom_Si = H_new.transpose()@(W[i]*(H_new@S[i]@H_new.transpose()))@H_new + 0.5*eta[i]
            S_new[i] = S[i] * (np.divide(num_Si, denom_Si)**0.5)
        
        # Frobenius norms for consecutive error
        f_norm_H = math.sqrt(np.sum((H_new - H)**2))
        f_norm_Si_sum = 0
        for i in range(0, len(A)):
            f_norm_Si_sum += math.sqrt(np.sum((S_new[i] - S[i])**2))
        f_norm_S = f_norm_Si_sum / len(A)
        f_norm = f_norm_H + f_norm_S
        
        # Update H and Si for next iteration
        H = H_new
        S = S_new
    
    return H, S


def WSSNMTF(A, k, tol):
    """
    Implement WSSNMTF if the adjacency matrix A is already formed
    Inputs:
        A: dict of adjacency matrices for N layers
        k: number of communities
        i: ith layer
    """
    W = get_W(A)
    eta = get_eta(A)
    H,S = get_H_and_S(A, W, eta, tol, k)
    return H, S


def normalize_H(H):
    """
    Normalize H such that each row add up to 1
    """
    row_sums = H.sum(axis=1, keepdims=True)
    normalized_H = H / row_sums
    return normalized_H


def plot_probabilities(normalized_H):
    """
    Plot the stacked bar plot for probabilities of nodes belonging to different communities
    """
    # Get the number of nodes and communities
    num_nodes, num_communities = normalized_H.shape
    # Create an array of node numbers
    nodes = np.arange(num_nodes)
    
    # Set up the stacked bar plot
    width = 1
    fig, ax = plt.subplots()
    bars = []
    bottom = np.zeros(num_nodes)
    colors = ["orange","grey","lightblue","lightgreen"]
    for i in range(0, num_communities):
        bar = ax.bar(nodes, normalized_H[:, i], width, bottom=bottom, label=f'Community {i}', color = colors[i])
        bars.append(bar)
        bottom += normalized_H[:, i]
    
    # Add labels and title
    ax.set_xlabel('Node Number')
    ax.set_ylabel('Probability')
    #ax.set_title('Probability of Nodes Belonging to Different Communities')
    #ax.set_xticks(nodes)
    
    #ax.set_xticklabels(nodes)
    ax.legend()

    # Show the plot
    plt.tight_layout()
    plt.show()
    
    
def actual_assignment(H):
    """
    Return an array indicating the communities the algorithm assigns for each node
    """
    # Find the column indices of the maximum elements in each row
    assignment = np.argmax(H, axis=1)
    return assignment


def expected_assignment(comm_division):
    """
    Return an array indicating the true community labels 
    Input: community division = array like [[0,99],[100,149],[150,299]]
    """
    array = []
    for i in range(0, len(comm_division)):
        for j in range(comm_division[i][0], comm_division[i][1]+1):
            array.append(i)
    return array


"""
Functions for constructing more informative adjacency matrices
"""

def identify_neighbors(matrix, node_index):
    """
    takes an adjacency matrix and the node index of interest
    returns an array of indices of the neighboring nodes
    """
    neighbors = np.nonzero(matrix[node_index])[0]
    neighbors = np.delete(neighbors, np.where(neighbors == node_index)) # excluding itself
    return neighbors


def SimRank(matrix, damping, max_iter=100, tol=1e-4):
    """
    takes an adjacency matrix and a damping factor rho ranging (0,1)
    returns the second proximity matrix computed using SimRank similarity
    """
    n = len(matrix)
    simrank_matrix = np.identity(n) # Initialize SimRank matrix with 1-diagonal
    for iter in range(max_iter):
        prev_simrank = np.copy(simrank_matrix)
        
        for i in range(n):
            for j in range(n):
                Ni = identify_neighbors(matrix, i)
                Nj = identify_neighbors(matrix, j)
                if (len(Ni)==0 or len(Nj)==0) == False:
                # Compute SimRank value for node pairs (i, j)
                    C = damping/(len(Ni)*len(Nj))
                    s = 0
                    for a in Ni:
                        for b in Nj:
                            s += prev_simrank[a][b]
                    simrank_matrix[i][j] = C * s
                    
        # Check for convergence
        if np.allclose(simrank_matrix, prev_simrank, atol=tol):
            break
            
    return simrank_matrix


def new_adjacency(matrix, weight, damping):
    """
    takes original matrix (not feature matrix), a weight parameter, and a damping factor for SimRank
    returns the new adjacency matrix 
    """
    first_prox = matrix
    second_prox = weight * SimRank(matrix, damping)
    return first_prox + second_prox


def feature_to_adjacency_matrix(feature_matrix):
    """
    takes a feature matrix
    returns adjacency matrix computed using cosine similarity
    """
    # Compute cosine similarity between feature vectors
    similarity_matrix = cosine_similarity(feature_matrix)
    # Set diagonal elements to zero
    np.fill_diagonal(similarity_matrix, 0)

    # Thresholding or normalization can be applied if needed
    # For example, setting a threshold to convert similarities to binary adjacency matrix:
    # adjacency_matrix = (similarity_matrix > threshold).astype(int)

    return similarity_matrix