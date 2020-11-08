import unittest
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_method(self):
        test_data = CsvReader("Tests/Data/Statistics.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.stats_mean(row['Value']), int(row['Mean']))
            self.assertEqual(self.statistics.result, int(row['Mean']))

    def test_median_method(self):
        test_data = CsvReader("Tests/Data/Statistics.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.stats_median(row['Value']), int(row['Median']))
            self.assertEqual(self.statistics.result, int(row['Median']))

    def test_mode_method(self):
        test_data = CsvReader("Tests/Data/Statistics.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.stats_mode(row['Value']), int(row['Mode']))
            self.assertEqual(self.statistics.result, int(row['Mode']))

    def test_Variance_method(self):
        test_data = CsvReader("Tests/Data/Statistics.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.stats_variance(row['Value']), int(row['Variance']))
            self.assertEqual(self.statistics.result, round(float(row['Variance']), 4))

    def test_standard_deviation(self):
        test_data = CsvReader("Tests/Data/Statistics.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.stats_standard_deviation(row['Value']), int(row['Standard_Deviation']))
            self.assertEqual(self.statistics.result, round(float(row['Standard_Deviation']), 5))


if __name__ == '__main__':
    unittest.main()
