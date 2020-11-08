from Statistics.Variance import variance
import math


def standard_deviation(data):
    var = variance(data)
    stand_dev = math.sqrt(var)
    return stand_dev
