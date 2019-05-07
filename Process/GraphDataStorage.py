from collections import namedtuple


class CurrentData:
    def __init__(self, appr_type, color):
        self.points = {}
        self.type = appr_type
        self.color = color

    def append(self, x, y, comp, perm, stab, interval):
        yi = namedtuple('yi', 'y, comp perm stab interval')
        self.points[x] = yi(y, comp, perm, stab, interval)


class GraphData:
    def __init__(self, heap_data, hoar_data, merge_data,
                 quad_data, shell_data):
        self.heap_data = heap_data
        self.hoar_data = hoar_data
        self.merge_data = merge_data
        self.quad_data = quad_data
        self.shell_data = shell_data
        self.data_list = [self.heap_data, self.hoar_data, self.merge_data,
                          self.quad_data, self.shell_data]
