from Statistics.Variance import variance
from Calculator.SquareRoot import sqrt


def standard_deviation(data):
    var = variance(data)
    return sqrt(var)
