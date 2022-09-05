import math

class Num:

    # `Num` summarizes a stream of numbers.

    def __init__(self,c=0,s="",w=""):
        self.n=0
        self.at=c
        self.name=s 
        self._has={}
        self.lo=math.inf   # lowest seen
        self.hi=-math.inf  # highest seen
        self.isSorted=True # No updates since last sort of data
        self.w=(s.find('-$')+1 and -1 or 1)
        
        