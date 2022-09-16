import math
import random
import collections
import re
from .Utils import Utils

"""
This method needs to be corrected later once we understand the data better.
"""
class Csv:
    def __init__(self):
        pass

    def csv(self, fname, fun=None, sep=None, src=None, s=None, t=None):
            sep = ","
            src = fname
            return True
            # Needs to be revisited.
            while True:
                with open(src) as f:
                    s = f.read()
                    if s:
                        t = {}
                        for s1 in s.split(','):
                            t[1+len(t)] = Utils.coerce(s1)
            