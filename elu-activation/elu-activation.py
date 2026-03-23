import numpy as np 

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here

    x = np.array(x)

    elu_x = np.where(x > 0, x, alpha * (np.exp(x) - 1))
    return elu_x.tolist()

    pass 

    #alt: boolean indexing
    """
    = np.array(x, dtype=float) # Ép kiểu float để tính toán chính xác
    
    # Tạo mặt nạ cho các phần tử <= 0
    mask = (x <= 0)
    
    # Chỉ thay đổi những vị trí thỏa mãn mask
    x[mask] = alpha * (np.exp(x[mask]) - 1)
    """