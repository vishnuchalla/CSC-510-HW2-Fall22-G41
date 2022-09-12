from code.Num import Num
from code.PrettyPrint import PrettyPrint

"""
Class to test utilities in the package.
"""

class TestUtils(object):
    """
    Init Method.
    """
    def __init__(self):
        self.the = {}

    """
    Method to test num method: The middle and diversity of a set of numbers is called "median"
    and "standard deviation" (and the latter is zero when all the nums are the same).
    """
    def test_num(self):
        num=Num()
        num.config = {'nums': 32}
        for i in range(1,101):
            num.add(i,0)
        mid,div = num.mid(), num.div(a=None)
        print(mid,div)
        return 50<=mid and mid<=52 and 30.5<div and div<32 and 32==len(num._has)

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
        self.the = ["james", {"test": {"sholay": "bond"}}, {"again": "crap"}]
        prettyPrint = PrettyPrint()
        result = prettyPrint.oo(self.the)
        return result == ["james", {"test": {"sholay": "bond"}}, {"again": "crap"}]