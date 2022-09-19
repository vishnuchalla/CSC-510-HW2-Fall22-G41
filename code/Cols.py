from .Num import Num
from .Sym import Sym
from .Utils import Utils


class Cols:

    def __init__(self, names):
        self.x = {}  # independent columns (that are not skipped)
        self.y = {}  # depedent columns (that are not skipped)
        self.all = {}  # all the columns (including the skipped ones)
        self.klass = None  # the single dependent klass column (if it exists)
        self.names = names  # all column names
        self.process_names(names)

    def process_names(self, names):
        for index, value in enumerate(names):
            # column that starts with upper case alphabet is num else sym
            col = Num(index, value) if value[0].isalpha() and value[0].isupper() else Sym(index, value)
            Utils.push(self.all, col)
            # print(self.all)
            if not value.endswith(':'):  # columns ending with ':' are skipped
                input_dict = self.y if any(value.endswith(i) for i in ['+', '!', '-']) else self.x
                Utils.push(input_dict, col)
                # print('x', self.x, 'y', self.y)
            if value.endswith('!'):
                self.klass = col


if __name__ == "__main__":  # Main method to test the functionality.
    Cols(['xyz:', 'yxz!', "abc+", "ball-"])
