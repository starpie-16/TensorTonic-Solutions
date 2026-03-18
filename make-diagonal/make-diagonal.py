import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    n = len(v)
    v = np.array(v)

    m = np.zeros((n, n))

    index = np.diag_indices(n) #(0, 0) (1, 1) ... (n-1, n-1)
    
    m[index] = v

    return m 
    pass
