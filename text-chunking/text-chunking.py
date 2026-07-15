def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    step = chunk_size - overlap
    res = []

    if not tokens:
        return []

    if chunk_size > len(tokens):
        res.append(tokens)
        return res


    for i in range(0, len(tokens), step):
        chunk_word = tokens[i: i+chunk_size]
        res.append(chunk_word)

        if i + chunk_size > len(tokens):
            break
            
    if len(res[-1]) < chunk_size:
        res.pop(-1)
    

    return res
        