import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.array(x)
    apply_tanh = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
    
    return apply_tanh
    pass