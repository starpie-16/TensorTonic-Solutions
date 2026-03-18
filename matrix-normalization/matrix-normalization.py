import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here

    

    matrix = np.array(matrix)

    if matrix.ndim != 2:
        return None

    if axis not in [None, 0, 1]:
        return None

    if norm_type not in ['l1', 'l2', 'max']:
        return None
    
    if axis is None:
        if norm_type == 'l2':
            total_norm = np.linalg.norm(matrix, axis = None)
            matrix_norm = matrix / total_norm

        if norm_type == 'l1':
            total_norm = np.linalg.norm(matrix, ord = 1, axis = None)
            matrix_norm = matrix / total_norm

        if norm_type == 'max':
            total_norm = np.max(np.abs(matrix))
            matrix_norm = matrix / total_norm

    if axis == 0:
        if norm_type == 'l2':
            total_norm = np.linalg.norm(matrix, axis = 0)
            matrix_norm = matrix / total_norm

        if norm_type == 'l1':
            total_norm = np.linalg.norm(matrix, ord = 1, axis = 0)
            matrix_norm = matrix / total_norm

        if norm_type == 'max':
            total_norm = np.max(np.abs(matrix), axis = 0)
            matrix_norm = matrix / total_norm

    if axis == 1:
        if norm_type == 'l2':
            total_norm = np.linalg.norm(matrix, axis = 1, keepdims = True)
            matrix_norm = matrix / total_norm

        if norm_type == 'l1':
            total_norm = np.linalg.norm(matrix, ord = 1, axis = 1, keepdims=True)
            matrix_norm = matrix / total_norm

        if norm_type == 'max':
            total_norm = np.max(np.abs(matrix), axis = 1, keepdims=True)
            matrix_norm = matrix / total_norm

    return np.nan_to_num(matrix_norm)
        
            
        
        
    
    pass