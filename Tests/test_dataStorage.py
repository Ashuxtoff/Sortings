import unittest
import os
import sys
from random import randint as rand
from copy import deepcopy
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Process.Calculate import Calculator
from Process.DataStorage import DataStorage, CurrentData, CurrentTypeStorage


class TestDataStorage(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        self.current_data_1 = CurrentData(rand(0, 10), rand(0, 10),
                                          rand(0, 10))
        self.current_data_1_copy = deepcopy(self.current_data_1)
        self.current_data_2 = CurrentData(rand(0, 10), rand(0, 10),
                                          rand(0, 10))
        self.current_data_2_copy = deepcopy(self.current_data_2)
        self.type_data_1 = self.calculator.make_current_type_data()
        self.type_data_1_copy = deepcopy(self.type_data_1)
        self.type_data_2 = self.calculator.make_current_type_data()
        self.type_data_2_copy = deepcopy(self.type_data_2)
        self.data_storage_1 = self.calculator.make_data_storage()
        self.data_storage_2 = self.calculator.make_data_storage()
        self.data_storage_1_copy = deepcopy(self.data_storage_1)
        self.data_storage_2_copy = deepcopy(self.data_storage_2)

    def test_current_data(self):
        self.current_data_1 += self.current_data_2
        self.assertEqual(self.current_data_1.time,
                         self.current_data_1_copy.time
                         + self.current_data_2.time)
        self.assertEqual(self.current_data_1.comparisons,
                         self.current_data_1_copy.comparisons
                         + self.current_data_2.comparisons)
        self.assertEqual(self.current_data_1.permutations,
                         self.current_data_1_copy.permutations
                         + self.current_data_2.permutations)
        self.current_data_2 /= 10
        self.assertEqual(self.current_data_2.time,
                         self.current_data_2_copy.time / 10)
        self.assertEqual(self.current_data_2.comparisons,
                         self.current_data_2_copy.comparisons / 10)
        self.assertEqual(self.current_data_2.permutations,
                         self.current_data_2_copy.permutations / 10)

    def test_current_type_storage(self):
        self.type_data_1 += self.type_data_2
        self.assertEqual(self.type_data_1.stability,
                         self.type_data_1_copy.stability
                         + self.type_data_2.stability)
        self.assertEqual(self.type_data_1.best_data,
                         self.type_data_1_copy.best_data
                         + self.type_data_2.best_data)
        self.assertEqual(self.type_data_1.random_data,
                         self.type_data_1_copy.random_data
                         + self.type_data_2.random_data)
        self.assertEqual(self.type_data_1.worst_data,
                         self.type_data_1_copy.worst_data
                         + self.type_data_2.worst_data)
        self.type_data_2 /= 10
        self.assertEqual(self.type_data_2.stability,
                         self.type_data_2_copy.stability / 10)
        self.assertEqual(self.type_data_2.best_data,
                         self.type_data_2_copy.best_data / 10)
        self.assertEqual(self.type_data_2.random_data,
                         self.type_data_2_copy.random_data / 10)
        self.assertEqual(self.type_data_2.worst_data,
                         self.type_data_2_copy.worst_data / 10)

    def test_data_storage(self):
        self.data_storage_1 += self.data_storage_2
        self.assertEqual(self.data_storage_1.heap_data,
                         self.data_storage_1_copy.heap_data
                         + self. data_storage_2.heap_data)
        self.assertEqual(self.data_storage_1.hoar_data,
                         self.data_storage_1_copy.hoar_data
                         + self. data_storage_2.hoar_data)
        self.assertEqual(self.data_storage_1.merge_data,
                         self.data_storage_1_copy.merge_data
                         + self. data_storage_2.merge_data)
        self.assertEqual(self.data_storage_1.quad_data,
                         self.data_storage_1_copy.quad_data
                         + self. data_storage_2.quad_data)
        self.assertEqual(self.data_storage_1.shell_data,
                         self.data_storage_1_copy.shell_data
                         + self. data_storage_2.shell_data)
        self.data_storage_2 /= 10
        self.assertEqual(self.data_storage_2.heap_data,
                         self.data_storage_2_copy.heap_data / 10)
        self.assertEqual(self.data_storage_2.hoar_data,
                         self.data_storage_2_copy.hoar_data / 10)
        self.assertEqual(self.data_storage_2.merge_data,
                         self.data_storage_2_copy.merge_data / 10)
        self.assertEqual(self.data_storage_2.quad_data,
                         self.data_storage_2_copy.quad_data / 10)
        self.assertEqual(self.data_storage_2.shell_data,
                         self.data_storage_2_copy.shell_data / 10)


if __name__ == '__main__':
    unittest.main()
