import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    # Write code here
    all_text = " ".join(documents)
    all_words = all_text.split()
    vocab = sorted(list(set(all_words)))

    vocab = sorted(list(set(all_words)))
    counts = np.array([[doc.split().count(word) for word in vocab] for doc in documents])    

    #1 TF
    row_sum = counts.sum(axis = 1, keepdims = True)
    tf = counts / row_sum

    #2 IDF
    df = (counts > 0).sum(axis = 0)
    n = counts.shape[0]
    idf = np.log(n/df)

    #3 TF-IDF
    tfidf_matrix = tf * idf

    return tfidf_matrix, vocab
    
    pass