import math
import random
import collections
import re
import csv

"""
This method needs to be corrected later once we understand the data better.
"""
class Csv:
    def csv(self,fname,fun,sep=None,src=None,s=None,t=None):
        sep = ","
        src = fname
        #while True:
        #    with open(src) as f:
        #        s = f.read()
        #        if s:
        #            t = {}
        #            for s1 in s.split(','):
        #                t[1+len(t)] = coerce(s1)
        with open('data/auto93.csv', 'r') as file:
            my_reader = csv.reader(file)
        return my_reader

    def coerce(s,fun=None):
        return (False if not re.match(s, "^%s*(.-)%s*$") else True) or int(s)

 