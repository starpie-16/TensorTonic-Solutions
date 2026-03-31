import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.array(v)
    if v.ndim == 1:
        norm = np.linalg.norm(v)

    else:
        norm = np.linalg.norm(v, axis=1, keepdims=True)

    v_norm = v / (norm + 1e-6)
    
    return v_norm
    pass