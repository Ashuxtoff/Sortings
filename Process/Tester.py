import os
import sys
import random
from timeit import default_timer as timer
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Sorters.HeapSort import HeapSorter
from Sorters.HoarSort import HoarSorter
from Sorters.MergeSort import MergeSorter
from Sorters.QuadraticSort import QuadraticSorter
from Sorters.ShellSort import ShellSorter
from Process.DataStorage import DataStorage, CurrentTypeStorage, CurrentData


class Tester:
    def __init__(self, random_array):
        self.random_array = random_array
        self.random_array_copy = self.random_array.copy()
        self.test_stability_array = [1 for i in range(len(self.random_array))]

    def measure_time(self, func, *args):
        start_time = timer()
        func(*args)
        return timer() - start_time

    def get_best_cases(self, sorter):
        if type(sorter) is MergeSorter:
            return sorted(self.random_array)[
                len(self.random_array)//2:] + sorted(self.random_array)[
                    :len(self.random_array)//2]
        else:
            return sorted(self.random_array)

    def get_worst_cases(self, sorter):
        if type(sorter) is HeapSorter:
            result = []
            for i in range(len(self.random_array)):
                if i == 0:
                    result.append(1000 * len(self.random_array))
                elif i % 2 == 1:
                    result.append(random.randint(result[(i - 1) // 2] - 1000,
                                  result[(i - 1) // 2] - 1))
                else:
                    result.append(random.randint(result[(i - 2) // 2] - 1000,
                                  result[(i - 2) // 2] - 1))
            return result
        if type(sorter) is HoarSorter:
            return self.random_array
        if type(sorter) is MergeSorter:
            array1 = sorted(self.random_array)[::2]
            array2 = sorted(self.random_array)[1:][::2]
            return array1 + array2
        if type(sorter) is QuadraticSorter:
            return sorted(self.random_array, reverse=True)
        if type(sorter) is ShellSorter:
            return sorted(self.random_array, reverse=True)

    def sortings_testing(self):
        for sorter_type in [HeapSorter, HoarSorter, MergeSorter,
                            QuadraticSorter, ShellSorter]:
            sorter = sorter_type()
            random_result = CurrentData(self.measure_time(sorter.sort,
                                                          self.random_array),
                                        sorter.comparisons,
                                        sorter.permutations)
            self.random_array = self.random_array_copy.copy()
            best_result = CurrentData(self.measure_time(sorter.sort,
                                                        self.get_best_cases(
                                                            sorter)),
                                      sorter.comparisons,
                                      sorter.permutations)
            self.random_array = self.random_array_copy.copy()
            if sorter_type is HoarSorter:
                worst_result = CurrentData(self.measure_time(
                    sorter.sort, self.get_worst_cases(sorter), -1),
                                           sorter.comparisons,
                                           sorter.permutations)
                self.random_array = self.random_array_copy.copy()
            else:
                worst_result = CurrentData(self.measure_time(
                    sorter.sort, self.get_worst_cases(sorter)),
                                           sorter.comparisons,
                                           sorter.permutations)
                self.random_array = self.random_array_copy.copy()
            sorter.sort(self.test_stability_array)
            if sorter_type is HeapSorter:
                heap_data = CurrentTypeStorage(random_result, worst_result,
                                               best_result,
                                               sorter.permutations)
            if sorter_type is HoarSorter:
                hoar_data = CurrentTypeStorage(random_result, worst_result,
                                               best_result,
                                               sorter.permutations)
            if sorter_type is MergeSorter:
                merge_data = CurrentTypeStorage(random_result, worst_result,
                                                best_result,
                                                sorter.permutations)
            if sorter_type is QuadraticSorter:
                quad_data = CurrentTypeStorage(random_result, worst_result,
                                               best_result,
                                               sorter.permutations)
            if sorter_type is ShellSorter:
                shell_data = CurrentTypeStorage(random_result, worst_result,
                                                best_result,
                                                sorter.permutations)
        return DataStorage(heap_data, hoar_data, merge_data,
                           quad_data, shell_data)
