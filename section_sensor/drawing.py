def drawing(freqs):
    return freqs.sample(n=10,weights="probs").index[0]
