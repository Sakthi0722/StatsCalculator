from Statistics.StandardDeviation import standard_deviation
from Statistics.Mean import mean
from Calculator.Division import division


def z_score(data):
    z = mean(data)
    stand_result = standard_deviation(data)
    z_list = []
    for i in data:
        z1 = round(division(stand_result, (i - z)), 5)
        z_list.append(z1)
    return z_list
