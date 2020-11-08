from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.StandardDeviation import standard_deviation
from Statistics.Variance import variance
from Statistics.ZScore import z_score


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def stats_mean(self, data):
        self.result = round(mean(data), 2)
        return self.result

    def stats_mode(self, data):
        self.result = mode(data)
        return self.result

    def stats_median(self, data):
        self.result = median(data)
        return self.result

    def stats_standard_deviation(self, data):
        self.result = round(standard_deviation(data), 3)
        return self.result

    def stats_variance(self, data):
        self.result = round(variance(data), 4)
        return self.result

    def stats_z_score(self, data):
        self.result = z_score(data)
        return self.result
