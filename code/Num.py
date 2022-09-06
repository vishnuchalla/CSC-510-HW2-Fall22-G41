import math
import random
import collections

class Num:

    # `Num` summarizes a stream of numbers.

    def __init__(self,c=0,s="",w="",config={}):
        self.n=0
        self.at=c
        self.name=s 
        self._has={}
        self.config = config
        self.lo=math.inf   # lowest seen
        self.hi=-math.inf  # highest seen
        self.isSorted=True # No updates since last sort of data
        self.w= (s.find('-$')+1 and -1 or 1)

    # Return the `p`-th thing from the sorted list `t`. - Move this to utility function afterwards
    def per(self, t, p):
        p=math.floor(((p or 0.5)*len(t))+ 0.5)
        
        return t[max(1,min(len(t),p))]

    # Return kept numbers, sorted
    def nums(self):
        if not self.isSorted:
            self._has=collections.OrderedDict(sorted(self._has.items()))
            self.isSorted=True
    
        return self._has

    # Reservoir sampler. Keep at most `the.nums` numbers
    # (and if we run out of room, delete something old, at random).,
    def add(self,v,pos):
        if v!="?":
            self.n=self.n+1
            self.lo=min(v, self.lo)
            self.hi=max(v, self.hi)

            if len(self._has)< self.config['nums']:
                pos=1+len(self._has)
            
            elif random.uniform(0,1) < self.config['nums']/self.n:
                pos=random.randrange(1, len(self._has))
            
            if pos:
                self.isSorted=False
                self._has[pos]= int(v)

    # Diversity (standard deviation for Nums, entropy for Syms)
    def div(self,a):
        a=self.nums()

        return (self.per(a,0.9)-self.per(a,0.1))/2.58

    # Central tendency (median for Nums, mode for Syms)
    def mid(self): 
        return self.per(self.nums(),0.5)