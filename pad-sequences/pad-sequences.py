import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    
    max_sent = max(len(seq) for seq in seqs)
    
    if max_len is None:
        max_len = max_sent
        

    pad_sent = np.full((len(seqs), max_len), fill_value = pad_value)

    for i, sent in enumerate(seqs):
        trunc_len = min(len(sent), max_len)
        pad_sent[i, :trunc_len] = sent[:trunc_len]

    return pad_sent        

    
    
    pass