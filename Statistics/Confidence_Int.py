from Statistics.StandardDeviation import standard_deviation
from Statistics.Mean import mean
import math


def confidence_interval(data):
    try:
        num_values = len(data)
        z = 1.96  # random z value
        stnd_dev = standard_deviation(data)
        mean_result = mean(data)
        return round(mean_result + (z * stnd_dev / math.sqrt(num_values)), 5)
    except ZeroDivisionError:
        print("ERROR: Can't divide by zero")
    except ValueError:
        print("ERROR: Check your input value type")