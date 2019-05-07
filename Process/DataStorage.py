class CurrentData:
    def __init__(self, time, comparisons, permutations):
        self.time = time
        self.comparisons = comparisons
        self.permutations = permutations

    def __add__(self, other):
        self.time += other.time
        self.comparisons += other.comparisons
        self.permutations += other.permutations
        return self

    def __truediv__(self, n):
        self.time /= n
        self.permutations /= n
        self.comparisons /= n
        return self

    def __sub__(self, other):
        return self.__add__(other/(-1))

    def __iadd__(self, other):
        return self.__add__(other)

    def __itruediv__(self, n):
        return self.__truediv__(n)

    def __eq__(self, other):
        cond_list = [self.time == other.time,
                     self.comparisons == other.comparisons,
                     self.permutations == other.permutations]
        for cond in cond_list:
            if not cond:
                return False
        return True


class CurrentTypeStorage:
    def __init__(self, random_data: CurrentData, worst_data: CurrentData,
                 best_data: CurrentData, stability):
        self.stability = stability
        self.random_data = random_data
        self.worst_data = worst_data
        self.best_data = best_data
        self.data_list = [self.random_data, self.worst_data, self.best_data]

    def __add__(self, other):
        self.random_data += other.random_data
        self.worst_data += other.worst_data
        self.best_data += other.best_data
        self.stability += other.stability
        self.data_list = [self.random_data, self.worst_data, self.best_data]
        return self

    def __truediv__(self, n):
        self.random_data /= n
        self.worst_data /= n
        self.best_data /= n
        self.stability /= n
        self.data_list = [self.random_data, self.worst_data, self.best_data]
        return self

    def __sub__(self, other):
        return self.__add__(other/(-1))

    def __iadd__(self, other):
        return self.__add__(other)

    def __itruediv__(self, n):
        return self.__truediv__(n)

    def __eq__(self, other):
        cond_list = [self.stability == other.stability,
                     self.worst_data == other.worst_data,
                     self.random_data == other.random_data,
                     self.best_data == other.best_data]
        for cond in cond_list:
            if not cond:
                return False
        return True


class DataStorage:
    def __init__(self, heap_data: CurrentTypeStorage,
                 hoar_data: CurrentTypeStorage,
                 merge_data: CurrentTypeStorage,
                 quad_data: CurrentTypeStorage,
                 shell_data: CurrentTypeStorage):
        self.heap_data = heap_data
        self.hoar_data = hoar_data
        self.merge_data = merge_data
        self.quad_data = quad_data
        self.shell_data = shell_data
        self.data_list = [self.heap_data, self.hoar_data, self.merge_data,
                          self.quad_data, self.shell_data]

    def __add__(self, other):
        self.heap_data += other.heap_data
        self.hoar_data += other.hoar_data
        self.merge_data += other.merge_data
        self.quad_data += other.quad_data
        self.shell_data += other.shell_data
        return self

    def __truediv__(self, n):
        self.heap_data /= n
        self.hoar_data /= n
        self.merge_data /= n
        self.quad_data /= n
        self.shell_data /= n
        return self

    def __sub__(self, other):
        return self.__add__(other/(-1))

    def __iadd__(self, other):
        return self.__add__(other)

    def __itruediv__(self, n):
        return self.__truediv__(n)

    def __eq__(self, other):
        cond_list = [self.heap_data == other.heap_data,
                     self.hoar_data == other.hoar_data,
                     self.merge_data == other.merge_data,
                     self.quad_data == other.quad_data,
                     self.shell_data == other.shell_data]
        for cond in cond_list:
            if not cond:
                return False
        return True
