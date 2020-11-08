from Statistics.StandardDeviation import standard_deviation
from Statistics.Mean import mean
from Calculator.Subtraction import subtraction
from Calculator.Division import division


def z_score(data):
    for i in range(len(data)):
        h = data[i] - mean(data)
        g = h / standard_deviation(data)
        return g

