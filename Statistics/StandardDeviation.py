import math
from Statistics.Variance import variance


def standard_deviation(data):
    var1 = variance(data)
    stud_dev = math.sqrt(var1)
    return stud_dev
