def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    my_dict = {
        
    }
    for sent in sentences:
        for w in sent:
            my_dict[w] = my_dict.get(w, 0) + 1

    return my_dict
            
    pass