import math
from .Csv import Csv
from .Cols import Cols
from .Utils import Row, Utils

class Data:
    def __init__(self, src):
        self.cols= None
        self.rows={}
        if type(src) is str:
            Csv.csv(src, 'add')
        else:
            for _,row in enumerate(src):
                self.add(row)

    def add(self, xs: Row):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            row = Utils.push(self.rows, xs if xs.cells else Row(xs))
            for todo in self.cols:
                for _,col in todo.y.items():
                    col.add(row.cells[col])

    def stats(self, places, showCols,fun,t,v):
        showCols = showCols if showCols else self.cols.y
        fun = fun if fun else 'mid'
        t = {}
        for _,col in showCols.items():
            # This function needs to be evaluated based on the type of the column
            # If col is a Symbol we need to call Sym or else Num.
            v = fun(col)
            v = type(v) in (int, float) and Utils.rnd(v,places) or v
            t[col.name] = v
        return t