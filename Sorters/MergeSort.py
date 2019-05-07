import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Sorters.BaseSorter import BaseSorter


class MergeSorter(BaseSorter):
    def __init__(self):
        self.comparisons = 0
        self.permutations = 0

    def sort(self, array):
        self.comparisons = 0
        self.permutations = 0
        if len(array) > 1:
            middle = len(array)//2
            left_half = array[:middle]
            right_half = array[middle:]

            self.sort(left_half)
            self.sort(right_half)

            i = 0
            j = 0
            k = 0
            while i < len(left_half) and j < len(right_half):
                self.comparisons += 1
                if left_half[i] < right_half[j]:
                    if array[k] != left_half[i]:
                        self.permutations += 1
                    array[k] = left_half[i]
                    i += 1
                else:
                    if array[k] != right_half[i]:
                        self.permutations += 1
                    array[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                if array[k] != left_half[i]:
                    self.permutations += 1
                array[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                if array[k] != right_half[j]:
                    self.permutations += 1
                array[k] = right_half[j]
                j += 1
                k += 1

        return array
