import unittest
import random
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Sorters.QuadraticSort import QuadraticSorter
from Sorters.MergeSort import MergeSorter
from Sorters.HeapSort import HeapSorter
from Sorters.HoarSort import HoarSorter
from Sorters.ShellSort import ShellSorter


class TestSortings(unittest.TestCase):
    def setUp(self):
        self.random_array = [random.randint(1, 1000) for i in range(1000)]

    def test_quadratic_sort_correctness(self):
        sorter = QuadraticSorter()
        handled = sorter.sort(self.random_array)
        for i in range(1, len(self.random_array)):
            self.assertTrue(handled[i] >= handled[i - 1])

    def test_merge_sort_correctness(self):
        sorter = MergeSorter()
        handled = sorter.sort(self.random_array)
        for i in range(1, len(self.random_array)):
            self.assertTrue(handled[i] >= handled[i - 1])

    def test_heap_sort_correctness(self):
        sorter = HeapSorter()
        handled = sorter.sort(self.random_array)
        for i in range(1, len(self.random_array)):
            self.assertTrue(handled[i] >= handled[i - 1])

    def test_hoar_sort_correctness(self):
        sorter = HoarSorter()
        handled = sorter.sort(self.random_array)
        for i in range(1, len(self.random_array)):
            self.assertTrue(handled[i] >= handled[i - 1])

    def test_shell_sort_correctness(self):
        sorter = ShellSorter()
        handled = sorter.sort(self.random_array)
        for i in range(1, len(self.random_array)):
            self.assertTrue(handled[i] >= handled[i - 1])


if __name__ == "__main__":
    unittest.main()
