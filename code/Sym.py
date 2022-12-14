import math

class Sym:

    # `Sym`s summarize a stream of symbols.

    def __init__(self,c=0,s=""):
        self.n=0
        self.at=c
        self.name=s 
        self._has={}
        
    # Add one thing to `col`. For Num, keep at most `nums` items.
    def add(self, v):
        if v!="?":
            self.n=self.n+1
            self._has[v]=1+self._has.setdefault(v,0)
        
    def mid(self, col=None, most=None, mode=None):
        most=-1
        for k,v in self._has.items():
            if v>most:
                mode,most=k,v
        
        return mode
        
    def div(self, e=None, fun=None):

        def fun(p):
            return p*math.log2(p)
        
        e=0
        for _,n in self._has.items():
            if n>0:
                e=e-fun(n/self.n)  
        
        return e


