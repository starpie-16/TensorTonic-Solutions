import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A = np.array(A)

    diag = np.diag(A)
    trace = diag.sum()

    return trace
    pass
