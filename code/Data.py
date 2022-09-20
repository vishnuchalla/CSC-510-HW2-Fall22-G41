import math

from code.Num import Num
from code.Sym import Sym
from code.Csv import Csv
from code.Cols import Cols
from code.Utils import Row, Utils


class Data:
    def __init__(self, src, sep=','):
        self.cols = None
        self.rows = {}
        csv = Csv()
        if type(src) is str:
            csv.csv(src, sep, self.add)
        else:
            for _, row in enumerate(src):
                self.add(row)

    def add(self, xs: Row):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            row = Utils().push(self.rows, xs if "cells" in xs else Row(xs))
            unskipped_col = []
            unskipped_col = list(self.cols.x.values()) + list(self.cols.y.values())
            for col in unskipped_col:
                col.add(row.cells[col.at])

    def stats(self, places, show_cols, fun, t=None, v=None):
        show_cols = show_cols if show_cols else self.cols.y
        fun = fun if fun else 'mid'
        t = {}
        for _, col in show_cols.items():
            # This function needs to be evaluated based on the type of the column
            # If col is a Symbol we need to call Sym or else Num.
            v = fun(col)
            v = Utils().rnd(v, places) if type(v) in (int, float) else v
            t[col.name] = v
        return t
