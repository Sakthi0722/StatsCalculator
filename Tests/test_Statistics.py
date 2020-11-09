import unittest
import numpy as np
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    test_data = []

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_method(self):
        test_data = CsvReader("Tests/Data/Mean.csv").data
        value_data = [int(row['Value 1']) for row in test_data]
        self.assertEqual(self.statistics.stats_mean(value_data), 22.67)
        self.assertEqual(self.statistics.result, 22.67)

    def test_median_method(self):
        test_data = CsvReader("Tests/Data/Median.csv").data
        value_data = [int(row['Value 1']) for row in test_data]
        self.assertEqual(self.statistics.stats_median(value_data), 22)
        self.assertEqual(self.statistics.result, 22)

    def test_mode_method(self):
        test_data = CsvReader("Tests/Data/Mode.csv").data
        value_data = [int(row['Value 1']) for row in test_data]
        self.assertEqual(self.statistics.stats_mode(value_data), [32])
        self.assertEqual(self.statistics.result, [32])

    def test_Variance_method(self):
        test_data = CsvReader("Tests/Data/Variance.csv").data
        value_data = [int(row['Value 1']) for row in test_data]
        self.assertEqual(self.statistics.stats_variance(value_data), np.var(value_data))
        self.assertEqual(self.statistics.result, np.var(value_data))

    def test_standard_deviation(self):
        test_data = CsvReader("Tests/Data/SD.csv").data
        value_data = [int(row['Value 1']) for row in test_data]
        self.assertEqual(self.statistics.stats_standard_deviation(value_data), np.std(value_data), 3)
        self.assertEqual(self.statistics.result, np.std(value_data))

    def test_z_score(self):
        test_data = CsvReader("Tests/Data/Z_Score.csv").data
        value_data = [int(row['Value 1']) for row in test_data]
        self.assertEqual(self.statistics.stats_z_score(value_data), -1.545686339706238)
        self.assertEqual(self.statistics.result, -1.545686339706238)

    def test_conf_int(self):
        test_data = CsvReader("Tests/Data/Z_Score.csv").data
        value_data = [int(row['Value 1']) for row in test_data]
        self.assertEqual(self.statistics.stats_conf_int(value_data), 26.81383)
        self.assertEqual(self.statistics.result, 26.81383)

    def test_marg_err(self):
        test_data = CsvReader("Tests/Data/Z_Score.csv").data
        value_data = [int(row['Value 1']) for row in test_data]
        self.assertEqual(self.statistics.stats_marg_err(value_data), 15.182094717133074)
        self.assertEqual(self.statistics.result, 15.182094717133074)

    def test_cochran(self):
        test_data = CsvReader("Tests/Data/Z_Score.csv").data
        value_data = [int(row['Value 1']) for row in test_data]
        self.assertEqual(self.statistics.stats_cochran(value_data), 0.004166666666666667)
        self.assertEqual(self.statistics.result, 0.004166666666666667)

    def test_samp_size(self):
        test_data = CsvReader("Tests/Data/Z_Score.csv").data
        value_data = [int(row['Value 1']) for row in test_data]
        self.assertEqual(self.statistics.stats_samp_size(value_data), 0.0009788673122310145)
        self.assertEqual(self.statistics.result, 0.0009788673122310145)


if __name__ == '__main__':
    unittest.main()
