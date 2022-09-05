import math
import random
import collections

class Num:

    # `Num` summarizes a stream of numbers.

    def __init__(self,c=0,s="",w=""):
        self.n=0
        self.at=c
        self.name=s 
        self._has={}
        self.lo= math.inf   # lowest seen
        self.hi= -math.inf  # highest seen
        self.isSorted=True # No updates since last sort of data
        self.w= (s.find('-$')+1 and -1 or 1)

    # Return the `p`-th thing from the sorted list `t`. - Move this to utility function afterwards
    def per(t,p):
        p=math.floor(((p or 0.5)*len(t))+ 0.5)
        
        return t[max(1,min(len(t),p))]
    
    