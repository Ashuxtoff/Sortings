import os
import sys
import random
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Sorters.BaseSorter import BaseSorter


class HoarSorter(BaseSorter):
    def __init__(self):
        self.comparisons = 0
        self.permutations = 0

    def sort(self, array, curr_pivot=None):
        self.comparisons = 0
        self.permutations = 0

        def divide_and_conquer(array):
            if len(array) <= 1:
                return array
            else:
                if curr_pivot == -1:
                    pivot = array[-1]
                else:
                    pivot = random.choice(array)
                greater_coeff = 0
                less_coeff = 0
                equal_coeff = 0
                greater = [x for x in array if x > pivot]
                equal = [x for x in array if x == pivot]
                less = [x for x in array if x < pivot]
                self.comparisons += 3*len(array)
                for i in range(len(array)):
                    if array[i] > pivot:
                        if i != len(less) + len(equal) + greater_coeff:
                            self.permutations += 1
                        greater_coeff += 1
                    if array[i] < pivot:
                        if i != less_coeff:
                            self.permutations += 1
                        less_coeff += 1
                    if array[i] == pivot:
                        if i != len(less) + equal_coeff:
                            self.permutations += 1
                        equal_coeff += 1
                return divide_and_conquer(
                    less) + equal + divide_and_conquer(greater)

        return divide_and_conquer(array)
