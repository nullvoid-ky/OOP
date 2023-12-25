def char_count(str):
    data = {}
    for c in str:
        if c in data:
            data[c] += 1
        else:
            data[c] = 1
    return data