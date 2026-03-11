import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    tokens = np.array(tokens)
    vocab = np.array(vocab)

    comparision_matrix = (vocab[:, None] == tokens)
    bow = comparision_matrix.sum(axis = 1)

    return bow
    pass