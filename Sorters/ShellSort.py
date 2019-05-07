import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Sorters.BaseSorter import BaseSorter


class ShellSorter(BaseSorter):
    def __init__(self):
        self.comparisons = 0
        self.permutations = 0

    def sort(self, array):
        self.comparisons = 0
        self.permutations = 0

        def gap_insertion_sort(array, start, gap):
            for i in range(start + gap, len(array), gap):
                current = array[i]
                self.comparisons += 1
                while i >= gap and array[i - gap] > current:
                    self.comparisons += 1
                    self.permutations += 1
                    array[i] = array[i - gap]
                    i = i - gap
                if array[i] != current:
                    self.permutations += 1
                array[i] = current

        sublist_len = len(array)//2
        while sublist_len > 0:
            for start in range(sublist_len):
                gap_insertion_sort(array, start, sublist_len)
            sublist_len = sublist_len // 2

        return array
