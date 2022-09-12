import math
import random
import collections
import csv
import Col
import Row

class Data:
   def __init__(self, src):
        self.xs=None
        self.cols= None
        self.rows={}
        if type(src) is str:
            csv(src, self.add(row))
        else:
            for _,row in len(src):
                self.add(row)

    def add(self, row):
        col = Col()
        if self.cols:
            self.cols = Cols(xs)
        else:
            row = push (self.rows, xs.cells and xs or Row(xs))
            for _,todo in cols.items():
                for _,col in len(todo):
                    col.add(row[col])

    def stats(self, places, showCols,fun,t,v):
        if not showCols:
            showCols = self.cols.y
        if not fun:
            fun = 'mid'
        t = {}
        for _,col in showCols.items:
            v = fun(col)
            v = type(v) is int and rnd(v,places) or v
            t[col.name] = v
        return t

    def push(t,x):
        t[1+len(t)] = x
    
    def rnd(x, places):
        mult = 10
        if places:
            mult = mult^places
        else:
            mult = mult^2
        return math.floor(x * mult + 0.5) / mult