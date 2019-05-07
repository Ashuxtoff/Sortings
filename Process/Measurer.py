import os
import sys
import random
from collections import namedtuple
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Process.Calculate import Calculator
from Process.Tester import Tester
from Sorters.HeapSort import HeapSorter
from Sorters.HoarSort import HoarSorter
from Sorters.ShellSort import ShellSorter
from Sorters.QuadraticSort import QuadraticSorter
from Sorters.MergeSort import MergeSorter


class Measurer:
    def make_input_data(self, length):
        return [random.randint(0, 1000) for i in range(length)]

    def __init__(self, data_length):
        self.calculator = Calculator()
        self.data_length = data_length
        self.random_data = self.make_input_data(data_length)

    def measure_data(self):
        tester = Tester(self.random_data)
        result = [tester.sortings_testing() for i in range(101)]
        return result

    def get_information(self):
        measuring_result = self.measure_data()
        average_time = self.calculator.calc_average_data(
            measuring_result)
        standart_deviations = self.calculator.calc_standart_deviations(
            measuring_result, average_time)
        confidence_interval = self.calculator.calc_confidence_intervals(
            standart_deviations)
        result_form = namedtuple('result',
                                 'average_time conf_interval stand_dev')
        result = result_form(average_time, confidence_interval,
                             standart_deviations)
        return result

    def get_orgered_information(self, information):
        data = information.average_time[-1]
        heap_time = {'best': data.heap_data.best_data.time,
                     'random': data.heap_data.random_data.time,
                     'worst': data.heap_data.worst_data.time}
        hoar_time = {'best': data.hoar_data.best_data.time,
                     'random': data.hoar_data.random_data.time,
                     'worst': data.hoar_data.worst_data.time}
        merge_time = {'best': data.merge_data.best_data.time,
                      'random': data.merge_data.random_data.time,
                      'worst': data.merge_data.worst_data.time}
        quad_time = {'best': data.quad_data.best_data.time,
                     'random': data.quad_data.random_data.time,
                     'worst': data.quad_data.worst_data.time}
        shell_time = {'best': data.shell_data.best_data.time,
                      'random': data.shell_data.random_data.time,
                      'worst': data.shell_data.worst_data.time}

        heap_comp = {'best': data.heap_data.best_data.comparisons,
                     'random': data.heap_data.random_data.comparisons,
                     'worst': data.heap_data.worst_data.comparisons}
        hoar_comp = {'best': data.hoar_data.best_data.comparisons,
                     'random': data.hoar_data.random_data.comparisons,
                     'worst': data.hoar_data.worst_data.comparisons}
        merge_comp = {'best': data.merge_data.best_data.comparisons,
                      'random': data.merge_data.random_data.comparisons,
                      'worst': data.merge_data.worst_data.comparisons}
        quad_comp = {'best': data.quad_data.best_data.comparisons,
                     'random': data.quad_data.random_data.comparisons,
                     'worst': data.quad_data.worst_data.comparisons}
        shell_comp = {'best': data.shell_data.best_data.comparisons,
                      'random': data.shell_data.random_data.comparisons,
                      'worst': data.shell_data.worst_data.comparisons}

        heap_perm = {'best': data.heap_data.best_data.permutations,
                     'random': data.heap_data.random_data.permutations,
                     'worst': data.heap_data.worst_data.permutations}
        hoar_perm = {'best': data.hoar_data.best_data.permutations,
                     'random': data.hoar_data.random_data.permutations,
                     'worst': data.hoar_data.worst_data.permutations}
        merge_perm = {'best': data.merge_data.best_data.permutations,
                      'random': data.merge_data.random_data.permutations,
                      'worst': data.merge_data.worst_data.permutations}
        quad_perm = {'best': data.quad_data.best_data.permutations,
                     'random': data.quad_data.random_data.permutations,
                     'worst': data.quad_data.worst_data.permutations}
        shell_perm = {'best': data.shell_data.best_data.permutations,
                      'random': data.shell_data.random_data.permutations,
                      'worst': data.shell_data.worst_data.permutations}

        heap_int = {'best': information.conf_interval[
                        HeapSorter][0][9],
                    'random': information.conf_interval[
                        HeapSorter][1][9],
                    'worst': information.conf_interval[
                        HeapSorter][2][9]}
        hoar_int = {'best': information.conf_interval[
                        HoarSorter][0][9],
                    'random': information.conf_interval[
                        HoarSorter][1][9],
                    'worst': information.conf_interval[
                        HoarSorter][2][9]}
        merge_int = {'best': information.conf_interval[
                        MergeSorter][0][9],
                     'random': information.conf_interval[
                        MergeSorter][1][9],
                     'worst': information.conf_interval[
                        MergeSorter][2][9]}
        quad_int = {'best': information.conf_interval[
                        QuadraticSorter][0][9],
                    'random': information.conf_interval[
                        QuadraticSorter][1][9],
                    'worst': information.conf_interval[
                        QuadraticSorter][2][9]}
        shell_int = {'best': information.conf_interval[
                        ShellSorter][0][9],
                     'random': information.conf_interval[
                        ShellSorter][1][9],
                     'worst': information.conf_interval[
                        ShellSorter][2][9]}

        heap_stab = data.heap_data.stability
        hoar_stab = data.hoar_data.stability
        merge_stab = data.merge_data.stability
        quad_stab = data.quad_data.stability
        shell_stab = data.shell_data.stability

        pattern_data_form = namedtuple('pattern_data',
                                       'best, random, worst')
        type_data_form = namedtuple('type_data',
                                    'time, comp, perm int stab')
        pattern_type_form = namedtuple('pattern_data',
                                       'heap, hoar, merge, quad, shell')

        def make_pattern_type_data(mode):
            heap = type_data_form(heap_time[mode], heap_comp[mode],
                                  heap_perm[mode], heap_int[mode],
                                  heap_stab)
            hoar = type_data_form(hoar_time[mode], hoar_comp[mode],
                                  hoar_perm[mode], hoar_int[mode],
                                  hoar_stab)
            merge = type_data_form(merge_time[mode], merge_comp[mode],
                                   merge_perm[mode], merge_int[mode],
                                   merge_stab)
            quad = type_data_form(quad_time[mode], quad_comp[mode],
                                  quad_perm[mode], quad_int[mode],
                                  quad_stab)
            shell = type_data_form(shell_time[mode], shell_comp[mode],
                                   shell_perm[mode], shell_int[mode],
                                   shell_stab)
            return pattern_type_form(heap, hoar, merge, quad, shell)

        return pattern_data_form(make_pattern_type_data('best'),
                                 make_pattern_type_data('random'),
                                 make_pattern_type_data('worst'))
