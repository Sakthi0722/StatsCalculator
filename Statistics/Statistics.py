from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.StandardDeviation import standard_deviation
from Statistics.Variance import variance
from Statistics.ZScore import z_score
from Statistics.Confidence_Int import confidence_interval
from Statistics.Margin_Error import margin_error
from Statistics.Cochran import cochran
from Statistics.Samp_Size import samp_size


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
        self.result = standard_deviation(data)
        return self.result

    def stats_variance(self, data):
        self.result = variance(data)
        return self.result

    def stats_z_score(self, data):
        self.result = z_score(data)
        return self.result

    def stats_conf_int(self, data):
        self.result = confidence_interval(data)
        return self.result

    def stats_marg_err(self, data):
        self.result = margin_error(data)
        return self.result

    def stats_cochran(self, data):
        self.result = cochran(data)
        return self.result

    def stats_samp_size(self, data):
        self.result = samp_size(data)
        return self.result
