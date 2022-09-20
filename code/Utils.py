import copy
import math
from code.PrettyPrint import PrettyPrint

class Row:
    def __init__(self, t):
        self.cells = t
        # deep copy needs to be implemented from scratch once we see the actual data.
        self.cooked = copy.deepcopy(t)
        self.isEvaled = False

class Utils:
    def __init__(self):
        self.n = 0

    def push(self, input_map, value):
        current_length = len(input_map)
        input_map[current_length+1] = value
        return value

    def rnd(self, x, places):
        mult = pow(10, (places if places else 2))
        return math.floor(x * mult + 0.5) / mult
    
    """
    Method to convert int, float and bool to respective
    types from csv.
    Sample Inputs: "12.23", "123", "true", "Clndrs"
    Sample Output: 12.23, 123, True/False, Clndrs
    """
    def coerce(self, s):
        def fun(s):
            if s == "true":
                return True
            elif s == "false":
                return False
            else:
                return s
        if s.isdigit():
            return int(s)
        else:
            try:
                return float(s)
            except ValueError:
                return fun(s)
    
    """
    Inline function used to log on first 10 lines of csv.
    Sample input: The entire csv file.
    Sample output: Only first 10 lines of it as stated below.
    {Clndrs Volume Hp: Lbs- Acc+ Model origin Mpg+}
    {8 304.0 193 4732 18.5 70 1 10}
    {8 360 215 4615 14 70 1 10}
    {8 307 200 4376 15 70 1 10}
    {8 318 210 4382 13.5 70 1 10}
    {8 429 208 4633 11 72 1 10}
    {8 400 150 4997 14 73 1 10}
    {8 350 180 3664 11 73 1 10}
    {8 383 180 4955 11.5 71 1 10}
    {8 350 160 4456 13.5 72 1 10}
    """
    def log(self, row):
        self.n += 1
        if(self.n > 10):
            return
        else:
            PrettyPrint().oo(row, sort=False)