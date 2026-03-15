def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    

    return [w for w in tokens if w not in stopwords]
    #stop_set = set(stopwords)
    #return [w for w in tokens if w not in stop_set]
    
    pass