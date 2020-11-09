from Statistics.StandardDeviation import standard_deviation
from Statistics.Mean import mean


def z_score(data):
    try:
        for i in range(len(data)):
            h = data[i] - mean(data)
            g = h / standard_deviation(data)
            return g
    except ZeroDivisionError:
        print("ERROR: Can't divide by zero")
    except ValueError:
        print("ERROR: Check your input value")
