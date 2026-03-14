import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here

    #1 khởi tạo trọng số và bias
    n_samples, n_features = X.shape
    w = np.zeros(n_features)
    b = 0

    for _ in range(steps):

        #1 forward
        z = np.dot(X, w) + b
        p = _sigmoid(z)

        #2 gradient descent
        dw = (1 / n_samples) * np.dot(X.T, (p - y)) #p-y là sai số
        db = (1 / n_samples) * np.sum(p - y)

        #3 update weight, bias
        w -= lr * dw
        b -= lr * db
        
    return w, b
        
    pass