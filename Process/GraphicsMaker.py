import os
import sys
import math
import matplotlib.pyplot as plt
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Sorters.HeapSort import HeapSorter
from Sorters.HoarSort import HoarSorter
from Sorters.MergeSort import MergeSorter
from Sorters.QuadraticSort import QuadraticSorter
from Sorters.ShellSort import ShellSorter
from Process.Measurer import Measurer
from Process.FuncsApproximator import FuncsApproximator


class GraphicsMaker:
    def __init__(self):
        self.approximator = FuncsApproximator()

    def make_approximated_graphic(self, data, pattern):
        plt.clf()
        for sort_type in data:
            if sort_type.type == 'a * lnx + b':
                a, b = self.approximator.log_approximate(sort_type)
                plt.plot([i for i in range(
                             2, max(list(sort_type.points.keys())) + 2)],
                         [a * math.log1p(i - 1) + max([0, b]) for i in range(
                             2, max(list(sort_type.points.keys())) + 2)],
                         sort_type.color)
            elif sort_type.type == 'a * x ** b':
                a, b = self.approximator.pow_approximate(sort_type)
                plt.plot([i for i in range(
                             max(list(sort_type.points.keys())) + 2)],
                         [a * (i ** b) for i in range(
                             max(list(sort_type.points.keys())) + 2)],
                         sort_type.color)
        plt.xlabel('Размер данных', fontsize=10)
        plt.ylabel('Время обработки, cек', fontsize=10)
        plt.savefig(pattern + '_appr.png')

    def make_points_graphic(self, data, pattern):
        plt.clf()
        for sort_type in data:
            xs = []
            ys = []
            intervals = []
            for x in sort_type.points:
                xs.append(x)
                ys.append(sort_type.points[x].y)
                intervals.append(sort_type.points[x].interval)
            plt.plot(xs, ys, 'ro', color=sort_type.color)
            for i in range(len(xs)):
                plt.plot((xs[i], xs[i]),
                         (ys[i]-intervals[i], ys[i]+intervals[i]),
                         color='black')
        plt.xlabel('Размер данных', fontsize=10)
        plt.ylabel('Время обработки, сек', fontsize=10)
        plt.savefig(pattern + '_points.png')

    def make_help_inf_graphic(self, data, mode, pattern):
        plt.clf()
        for sort_type in data:
            xs = []
            help_inf = []
            for x in sort_type.points:
                xs.append(x)
                if mode == 'comps':
                    help_inf.append(sort_type.points[x].comp / 1000)
                    plt.ylabel('Количество сравнений, тыс', fontsize=10)
                if mode == 'perms':
                    help_inf.append(sort_type.points[x].perm / 1000)
                    plt.ylabel('Количество перестановок, тыс', fontsize=10)
            plt.plot(xs, help_inf, 'ro', color=sort_type.color)
        plt.xlabel('Размер данных', fontsize=10)
        plt.savefig(pattern + '_' + mode + '.png')

    def make_stability_graphic(self, data):
        plt.clf()
        for sort_type in data:
            xs = []
            stab_factors = []
            for x in sort_type.points:
                xs.append(x)
                stab_factors.append(sort_type.points[x].stab / 1000)
            plt.plot(xs, stab_factors, 'ro', color=sort_type.color)
        plt.xlabel('Размер данных', fontsize=10)
        plt.ylabel('Перестановки, тыс', fontsize=10)
        plt.savefig('stab.png')
