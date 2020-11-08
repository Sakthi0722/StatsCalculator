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


if __name__ == '__main__':
    unittest.main()
