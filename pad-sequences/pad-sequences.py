import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    lens = np.array([len(s) for s in seqs])

    if max_len is None:
        target_len = lens.max()
    else:
        target_len = max_len
        

    truncated_seqs = [np.array(s[:target_len]) for s in seqs]

    final_lens = np.minimum(lens, target_len)

    mask = np.arange(target_len) < final_lens[:, None]

    res = np.full((len(seqs), target_len), pad_value, dtype=int)
    
    res[mask] = np.concatenate(truncated_seqs)

    return res
    
    
                      
    pass