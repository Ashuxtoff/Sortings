import os
import sys
from collections import namedtuple
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Sorters.HeapSort import HeapSorter
from Sorters.HoarSort import HoarSorter
from Sorters.MergeSort import MergeSorter
from Sorters.QuadraticSort import QuadraticSorter
from Sorters.ShellSort import ShellSorter
from Process.Measurer import Measurer
from Process.GraphDataStorage import CurrentData, GraphData
from Process.GraphicsMaker import GraphicsMaker


class Runner:
    def __init__(self, start, step, stop):
        self.start = start
        self.step = step
        self.stop = stop
        self.graphics_maker = GraphicsMaker()
        self.full_best_data = GraphData(CurrentData('a * lnx + b', 'blue'),
                                        CurrentData('a * lnx + b', 'green'),
                                        CurrentData('a * lnx + b', 'pink'),
                                        CurrentData('a * x ** b', 'red'),
                                        CurrentData('a * lnx + b', 'orange'))
        self.full_random_data = GraphData(CurrentData('a * lnx + b', 'blue'),
                                          CurrentData('a * lnx + b', 'green'),
                                          CurrentData('a * lnx + b', 'pink'),
                                          CurrentData('a * x ** b', 'red'),
                                          CurrentData('a * lnx + b', 'orange'))
        self.full_worst_data = GraphData(CurrentData('a * lnx + b', 'blue'),
                                         CurrentData('a * x ** b', 'green'),
                                         CurrentData('a * lnx + b', 'pink'),
                                         CurrentData('a * x ** b', 'red'),
                                         CurrentData('a * x ** b', 'orange'))

    def run(self):

        def make_full_data(i, ordered_data, mode):
            if mode == 'best':
                current = self.full_best_data
                data = ordered_data.best
            if mode == 'random':
                current = self.full_random_data
                data = ordered_data.random
            if mode == 'worst':
                current = self.full_worst_data
                data = ordered_data.worst
            current.heap_data.append(i, data.heap.time,
                                     data.heap.comp, data.heap.perm,
                                     data.heap.stab, data.heap.int)
            current.hoar_data.append(i, data.hoar.time,
                                     data.hoar.comp, data.hoar.perm,
                                     data.hoar.stab, data.hoar.int)
            current.merge_data.append(i, data.merge.time,
                                      data.merge.comp, data.merge.perm,
                                      data.merge.stab, data.merge.int)
            current.quad_data.append(i, data.quad.time,
                                     data.quad.comp, data.quad.perm,
                                     data.quad.stab, data.quad.int)
            current.shell_data.append(i, data.shell.time,
                                      data.shell.comp, data.shell.perm,
                                      data.shell.stab, data.shell.int)

        for i in range(self.start, self.stop, self.step):
            measurer = Measurer(i)
            data = measurer.get_information()
            ordered_data = measurer.get_orgered_information(data)

            make_full_data(i, ordered_data, 'best')
            make_full_data(i, ordered_data, 'random')
            make_full_data(i, ordered_data, 'worst')

        def graphics(data_list, pattern):
            self.graphics_maker.make_approximated_graphic(data_list, pattern)
            self.graphics_maker.make_points_graphic(data_list, pattern)
            self.graphics_maker.make_help_inf_graphic(data_list, 'comps',
                                                      pattern)
            self.graphics_maker.make_help_inf_graphic(data_list, 'perms',
                                                      pattern)

        graphics(self.full_best_data.data_list, 'best')
        graphics(self.full_random_data.data_list, 'random')
        graphics(self.full_worst_data.data_list, 'worst')
        self.graphics_maker.make_stability_graphic(
            self.full_random_data.data_list)


for i in range(3):  # Прогрев кеша
    runner = Runner(10, 10, 50)
    runner.run()

runner = Runner(100, 100, 1000)
runner.run()
