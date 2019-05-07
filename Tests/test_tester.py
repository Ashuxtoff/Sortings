import os
import sys
import unittest
import math
import time
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Process.Tester import Tester
from Sorters.HeapSort import HeapSorter
from Sorters.HoarSort import HoarSorter
from Sorters.MergeSort import MergeSorter
from Sorters.QuadraticSort import QuadraticSorter
from Sorters.ShellSort import ShellSorter


class TestTester(unittest.TestCase):
    def setUp(self):
        self.random_array = [23, 56, 12, 76, 45, 3, 90,
                             4, 29, 62, 86, 56, 21, 89]
        self.tester = Tester(self.random_array)

    def test_get_best_cases(self):
        sorter = MergeSorter()
        result = self.tester.get_best_cases(sorter)
        first = result[:len(result)//2]
        second = result[len(result)//2:]
        for i in range(min(len(first), len(second))):
            self.assertGreaterEqual(first[i], second[i])
        for i in range(1, len(first)):
            self.assertGreaterEqual(first[i], first[i-1])
        for i in range(1, len(second)):
            self.assertGreaterEqual(second[i], second[i-1])
        for sorter_type in [HeapSorter, HoarSorter,
                            QuadraticSorter, ShellSorter]:
            sorter = sorter_type()
            result = self.tester.get_best_cases(sorter)
            for i in range(1, len(result)):
                self.assertGreaterEqual(result[i], result[i-1])

    def test_get_worst_cases(self):
        for sorter_type in [HeapSorter, HoarSorter, MergeSorter,
                            QuadraticSorter, ShellSorter]:
            sorter = sorter_type()
            result = self.tester.get_worst_cases(sorter)
            if sorter_type is HeapSorter:
                for i in range(1, len(result)):
                    self.assertGreater(result[0], result[i])
                for i in range(len(result)-1, 1, -1):
                    self.assertLess(result[i], result[math.ceil(i/2)-1])
            if sorter_type is HoarSorter:
                for i in range(len(result)):
                    self.assertEquals(result[i], self.random_array[i])
            if sorter_type is MergeSorter:
                for i in range(len(result)//2):
                    self.assertGreaterEqual(result[i+len(result)//2],
                                            result[i])
            if sorter_type is QuadraticSorter or sorter_type is ShellSorter:
                for i in range(1, len(result)):
                    self.assertLessEqual(result[i], result[i-1])

    def test_measure_time(self):
        def sleep_a_second(added_time):
            time.sleep(1 + added_time)

        self.assertLess(3 - self.tester.measure_time(sleep_a_second, 2), 0.1)


if __name__ == "__main__":
    unittest.main()
