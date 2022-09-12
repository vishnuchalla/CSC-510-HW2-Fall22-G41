import copy

class Row:
    def __init__(self, t):
        self.cells = t
        # deep copy needs to be implemented from scratch once we see the actual data.
        self.cooked = copy.deepcopy(t)
        self.isEvaled = False