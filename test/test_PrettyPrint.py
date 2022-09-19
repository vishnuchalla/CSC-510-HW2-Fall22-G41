from code.Num import Num
from code.PrettyPrint import PrettyPrint

"""
Class to test utilities in the package.
"""

class TestPrettyPrint(object):
    """
    Init Method.
    """
    def __init__(self):
        self.the = {}

    """
    Method to test big num method: Nums store only a sample of the numbers added to it (and that storage
    is done such that the kept numbers span the range of inputs).
    """
    def test_bigNum(self):
        self.the['nums']=32
        num=Num(config=self.the)
        prettyPrint = PrettyPrint()
        for i in range(1,1001):
            num.add(i, 0)
        prettyPrint.oo(num.nums())
        return 32==len(num._has)
    
    """
    Method to test the.
    """
    def test_the(self):
        self.the['nums']=32
        prettyPrint = PrettyPrint()
        prettyPrint.oo(self.the)
        return True
    
    """
    Method to test oo with complex json.
    """
    def test_oo(self):
        self.the = [{"dump": "flase"}, {"eg": "ALL"},{"file":"../data/auto93.csv"},{"help":"true"},{"nums":"512"},{"seed":"10019"},{"seperator":","}]
        prettyPrint = PrettyPrint()
        result = prettyPrint.oo(self.the)
        return result == [{"dump": "flase"}, {"eg": "ALL"},{"file":"../data/auto93.csv"},{"help":"true"},{"nums":"512"},{"seed":"10019"},{"seperator":","}]