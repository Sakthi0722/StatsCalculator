import unittest
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_method(self):
        test_data = CsvReader("Tests/Data/Mean.csv").data
        value_data = [int(row['Value 1']) for row in test_data]
        for row in test_data:
            self.assertEqual(self.statistics.stats_mean(value_data), int(row['Mean']))
            self.assertEqual(self.statistics.result, int(row['Mean']))

    def test_median_method(self):
        test_data = CsvReader("Tests/Data/Median.csv").data
        value_data = [int(row['Value 1']) for row in test_data]
        for row in test_data:
            self.assertEqual(self.statistics.stats_median(value_data), int(row['Median']))
            self.assertEqual(self.statistics.result, int(row['Median']))

    def test_mode_method(self):
        test_data = CsvReader("Tests/Data/Mode.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.stats_mode(row['Value 1']), int(row['Mode']))
            self.assertEqual(self.statistics.result, int(row['Mode']))

    def test_Variance_method(self):
        test_data = CsvReader("Tests/Data/Variance.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.stats_variance(row['Value 1']), int(row['Variance']))
            self.assertEqual(self.statistics.result, round(float(row['Variance']), 4))

    def test_standard_deviation(self):
        test_data = CsvReader("Tests/Data/SD.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.stats_standard_deviation(row['Value 1']), int(row['Standard_Deviation']))
            self.assertEqual(self.statistics.result, round(float(row['Standard_Deviation']), 5))


if __name__ == '__main__':
    unittest.main()
