import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Sorters.BaseSorter import BaseSorter


class HeapSorter(BaseSorter):
    def __init__(self):
        self.comparisons = 0
        self.permutations = 0

    def sort(self, array):
        self.comparisons = 0
        self.permutations = 0

        def swap_items(index1, index2):
            self.comparisons += 1
            if array[index1] < array[index2]:
                self.permutations += 1
                array[index1], array[index2] = array[index2], array[index1]

        def sift_down(parent, limit):
            while True:
                child = (parent + 1) << 1  # То же, что и parent * 2 + 2
                if child < limit:
                    self.comparisons += 1
                    if array[child] < array[child - 1]:
                        child -= 1
                    swap_items(parent, child)
                    parent = child
                else:
                    break

        length = len(array)
        for i in range((length >> 1) - 1, -1, -1):
            sift_down(i, length)
        for i in range(length - 1, 0, -1):
            swap_items(i, 0)
            sift_down(0, i)

        return array
