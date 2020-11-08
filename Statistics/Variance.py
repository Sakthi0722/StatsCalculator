from Calculator.Square import square


def variance(data):
    num_values = len(data)
    total = 0
    for i in data:
        total = total + square(i)
    return (num_values - 1) / total
