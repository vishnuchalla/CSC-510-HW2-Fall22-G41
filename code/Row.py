class Row:
    def __init__(self, t):
        self.cells = t  # one record
        self.cooked = t.copy()  # used if we discretize data
        self.isEvaled = False  # true if y-values evaluated


