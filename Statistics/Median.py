def median(data):
    n = len(data)
    index = n // 2
    if n % 2:
        return sorted(data)[index]
    else:
        sum(sorted(data)[index - 1:index + 1]) / 2
