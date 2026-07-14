import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    num_seqs = len(seqs)
    max_sent = max(len(seq) for seq in seqs)

    if max_len is None:
        max_len = max_sent

    pad_sent = np.full((num_seqs, max_len), fill_value = pad_value)

    lens = np.array([min(len(s), max_len) for s in seqs])

    col_indices = np.arange(max_len)

    mask = col_indices < lens[:, None]

    flat_vals = np.concatenate([np.asarray(s[:max_len]) for s in seqs])

    pad_sent[mask] = flat_vals

    return pad_sent


    
    pass