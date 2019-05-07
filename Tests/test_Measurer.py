import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Process.Measurer import Measurer
from Sorters.HeapSort import HeapSorter
from Sorters.HoarSort import HoarSorter
from Sorters.MergeSort import MergeSorter
from Sorters.QuadraticSort import QuadraticSorter
from Sorters.ShellSort import ShellSorter


class TestMeasurer(unittest.TestCase):
    def setUp(self):
        self.measurer = Measurer(10)

    def test_get_ordered_information(self):
        information = self.measurer.get_information()
        result = self.measurer.get_orgered_information(information)
        average = information.average_time[-1]
        intervals = information.conf_interval
        self.assertEqual(average.heap_data.best_data.time,
                         result.best.heap.time)
        self.assertEqual(average.hoar_data.best_data.time,
                         result.best.hoar.time)
        self.assertEqual(average.merge_data.best_data.time,
                         result.best.merge.time)
        self.assertEqual(average.quad_data.best_data.time,
                         result.best.quad.time)
        self.assertEqual(average.shell_data.best_data.time,
                         result.best.shell.time)
        self.assertEqual(average.heap_data.best_data.comparisons,
                         result.best.heap.comp)
        self.assertEqual(average.hoar_data.best_data.comparisons,
                         result.best.hoar.comp)
        self.assertEqual(average.merge_data.best_data.comparisons,
                         result.best.merge.comp)
        self.assertEqual(average.quad_data.best_data.comparisons,
                         result.best.quad.comp)
        self.assertEqual(average.shell_data.best_data.comparisons,
                         result.best.shell.comp)
        self.assertEqual(average.heap_data.best_data.permutations,
                         result.best.heap.perm)
        self.assertEqual(average.hoar_data.best_data.permutations,
                         result.best.hoar.perm)
        self.assertEqual(average.merge_data.best_data.permutations,
                         result.best.merge.perm)
        self.assertEqual(average.quad_data.best_data.permutations,
                         result.best.quad.perm)
        self.assertEqual(average.shell_data.best_data.permutations,
                         result.best.shell.perm)
        self.assertEqual(average.heap_data.stability,
                         result.best.heap.stab)
        self.assertEqual(average.hoar_data.stability,
                         result.best.hoar.stab)
        self.assertEqual(average.merge_data.stability,
                         result.best.merge.stab)
        self.assertEqual(average.quad_data.stability,
                         result.best.quad.stab)
        self.assertEqual(average.shell_data.stability,
                         result.best.shell.stab)
        self.assertEqual(result.best.heap.int,
                         intervals[HeapSorter][0][9])
        self.assertEqual(result.best.hoar.int,
                         intervals[HoarSorter][0][9])
        self.assertEqual(result.best.merge.int,
                         intervals[MergeSorter][0][9])
        self.assertEqual(result.best.quad.int,
                         intervals[QuadraticSorter][0][9])
        self.assertEqual(result.best.shell.int,
                         intervals[ShellSorter][0][9])


if __name__ == '__main__':
    unittest.main()
