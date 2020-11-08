

def variance(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x-mean) **2 for x in data]
    var = sum(deviations) / n
    return var
