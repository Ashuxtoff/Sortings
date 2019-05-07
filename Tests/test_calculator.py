import sys
import os
import unittest
import math
from copy import deepcopy
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Sorters.HeapSort import HeapSorter
from Sorters.HoarSort import HoarSorter
from Sorters.MergeSort import MergeSorter
from Sorters.QuadraticSort import QuadraticSorter
from Sorters.ShellSort import ShellSorter
from Process.Calculate import Calculator
from Process.DataStorage import DataStorage, CurrentData, CurrentTypeStorage


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        self.data_list = [self.calculator.make_data_storage()
                          for i in range(4)]
        self.data_list_copy = deepcopy(self.data_list)
        self.long_data_list = [self.calculator.make_data_storage()
                               for i in range(104)]

    def test_calc_average_data(self):
        result = self.calculator.calc_average_data(self.data_list)
        self.assertEqual(result[0], self.data_list[0])
        self.assertEqual(result[1], (self.data_list[0]
                                     + self.data_list[1]) / 2)
        self.assertEqual(result[3], (self.data_list_copy[0]
                                     + self.data_list_copy[1]
                                     + self.data_list_copy[2]
                                     + self.data_list_copy[3]) / 4)

    def test_calc_confidence_interval(self):
        intervals_list = [6, 11, 16, 21, 26, 31, 36, 41, 51, 101]
        average_data = self.calculator.calc_average_data(self.long_data_list)
        stand_devs = self.calculator.calc_standart_deviations(
            self.long_data_list, average_data)
        intervals = self.calculator.calc_confidence_intervals(stand_devs)
        for sorter in self.calculator.types_list:
            for j in range(3):
                for i in range(len(intervals_list)):
                    number = intervals_list[i]
                    self.assertEqual(intervals[sorter][j][i],
                                     self.calculator.confidence_intervals_dict[
                                        number] * stand_devs[
                                            number - 3][sorter][
                                                j] / math.sqrt(number)
                                     )

    def test_calc_standart_deviations(self):
        average_data = self.calculator.calc_average_data(self.data_list)
        stand_devs = self.calculator.calc_standart_deviations(
            self.data_list, average_data)
        types_dict = {HeapSorter: 0, HoarSorter: 1, MergeSorter: 2,
                      QuadraticSorter: 3, ShellSorter: 4}
        for sorter in self.calculator.types_list:
            for j in range(3):
                self.assertEqual(stand_devs[0][sorter][j],
                                 math.fabs(self.data_list[1].data_list[
                                     types_dict[sorter]].data_list[j].time
                                 - average_data[1].data_list[types_dict[
                                     sorter]].data_list[j].time))


if __name__ == '__main__':
    unittest.main()
