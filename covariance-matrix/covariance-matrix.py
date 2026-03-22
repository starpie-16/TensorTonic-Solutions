import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here

    

    X = np.array(X)

    if X.shape[0] <= 1:
        return None

    if X.ndim != 2:
        return None

    
    cov_matrix = np.cov(X.T)
    return np.array(cov_matrix).reshape(1, 1) if cov_matrix.ndim == 0 else cov_matrix
    pass

    