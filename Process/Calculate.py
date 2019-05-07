import math
import os
import sys
from copy import deepcopy
from random import randint as rand
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Sorters.HeapSort import HeapSorter
from Sorters.HoarSort import HoarSorter
from Sorters.MergeSort import MergeSorter
from Sorters.QuadraticSort import QuadraticSorter
from Sorters.ShellSort import ShellSorter
from Process.DataStorage import DataStorage, CurrentTypeStorage, CurrentData


class Calculator:
    def __init__(self):
        self.types_list = [HeapSorter, HoarSorter, MergeSorter,
                           QuadraticSorter, ShellSorter]
        self.confidence_intervals_dict = {6: 2.5706, 11: 2.2281, 16: 2.1314,
                                          21: 2.0860, 26: 2.0555, 31: 2.0423,
                                          36: 2.0301, 41: 2.0211, 51: 2.0086,
                                          101: 1.9840}

    def make_current_type_data(self, mode=None):
        if mode == 'default':
            result_list = [CurrentData(0, 0, 0) for i in range(3)]
            result_list.append(0)
        else:
            result_list = [CurrentData(rand(0, 10), rand(0, 10), rand(0, 10))
                           for i in range(3)]
            result_list.append(rand(0, 10))
        return CurrentTypeStorage(*result_list)

    def make_data_storage(self, mode=None):
        if mode == 'default':
            return DataStorage(*[self.make_current_type_data('default'),
                                 self.make_current_type_data('default'),
                                 self.make_current_type_data('default'),
                                 self.make_current_type_data('default'),
                                 self.make_current_type_data('default')])
        return DataStorage(*[self.make_current_type_data(),
                             self.make_current_type_data(),
                             self.make_current_type_data(),
                             self.make_current_type_data(),
                             self.make_current_type_data()])

    def calc_average_data(self, data_list):
        current_data = self.make_data_storage('default')
        result_list = []
        for i in range(len(data_list)):
            current_data += data_list[i]
            result_list.append(deepcopy(current_data) / (i + 1))
        return result_list

    def calc_standart_deviations(self, data, average_data):

        def make_result_list(data, average_data, sorter, result_list):
            types_dict = {HeapSorter: 0, HoarSorter: 1, MergeSorter: 2,
                          QuadraticSorter: 3, ShellSorter: 4}
            result_list[0][sorter] = [math.fabs(data[1].data_list[
                types_dict[sorter]].data_list[0].time - average_data[
                    1].data_list[types_dict[sorter]].data_list[0].time),
                                      math.fabs(data[1].data_list[
                                          types_dict[sorter]].data_list[
                                              1].time - average_data[
                                                  1].data_list[types_dict[
                                                      sorter]].data_list[
                                                          1].time),
                                      math.fabs(data[1].data_list[
                                          types_dict[sorter]].data_list[
                                              2].time - average_data[
                                                  1].data_list[types_dict[
                                                      sorter]].data_list[
                                                          2].time)]

            for i in range(1, len(result_list)):
                for j in range(3):
                    last_res_quad = math.pow(result_list[i-1][sorter][j], 2)
                    last_res_quad *= i
                    new_time = data[i+1].data_list[types_dict[
                        sorter]].data_list[j].time
                    average_new_time = average_data[i+1].data_list[
                        types_dict[sorter]].data_list[j].time
                    new_member = math.pow(new_time - average_new_time, 2)
                    last_res_quad += new_member
                    last_res_quad /= (i + 1)
                    result_list[i][sorter][j] = math.sqrt(last_res_quad)

        data_dict = {HeapSorter: [0, 0, 0],
                     HoarSorter: [0, 0, 0],
                     MergeSorter: [0, 0, 0],
                     QuadraticSorter: [0, 0, 0],
                     ShellSorter: [0, 0, 0]}
        result_list = []
        for i in range(1, len(data)):
            result_list.append(data_dict.copy())
        for current_type in self.types_list:
            make_result_list(data, average_data, current_type, result_list)

        return result_list

    def calc_confidence_intervals(self, deviations_list):
        numbers = [6, 11, 16, 21, 26, 31, 36, 41, 51, 101]
        result_dict = {
            HeapSorter: [[], [], []],
            HoarSorter: [[], [], []],
            MergeSorter: [[], [], []],
            QuadraticSorter: [[], [], []],
            ShellSorter: [[], [], []]
        }
        for sorter in self.types_list:
            for i in range(len(numbers)):
                for j in range(3):
                    number = numbers[i]
                    conf_interval = self.confidence_intervals_dict[
                        number] * deviations_list[
                        number - 3][sorter][j] / math.sqrt(number)
                    result_dict[sorter][j].append(conf_interval)
        return result_dict
