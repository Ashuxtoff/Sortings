import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Sorters.BaseSorter import BaseSorter


class QuadraticSorter(BaseSorter):
    def __init__(self):
        self.comparisons = 0
        self.permutations = 0

    def sort(self, array):
        for i in range(len(array)):
            for j in range(len(array) - 1, i, -1):
                self.comparisons += 1
                if array[j] < array[j - 1]:
                    self.permutations += 2
                    array[j], array[j - 1] = array[j - 1], array[j]

        return array
