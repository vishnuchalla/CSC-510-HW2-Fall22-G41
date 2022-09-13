import copy
import math

class Row:
    def __init__(self, t):
        self.cells = t
        # deep copy needs to be implemented from scratch once we see the actual data.
        self.cooked = copy.deepcopy(t)
        self.isEvaled = False

class Utils:
    def __init__(self):
        pass

    def push(self, input_map, value):
        current_length = len(input_map)
        input_map[current_length+1] = value
        return value

    def rnd(self, x, places):
        mult = pow(10, (places if places else 2))
        return math.floor(x * mult + 0.5) / mult