from code.Num import Num
from code.PrettyPrint import PrettyPrint
import Framework

"""
Class to test utilities in the package.
"""

class TestPrettyPrint(object):
    """
    Init Method.
    """
    def __init__(self):
        self.the = Framework.updated_the

    """
    Method to test big num method: Nums store only a sample of the numbers added to it (and that storage
    is done such that the kept numbers span the range of inputs).
    """
    def test_bigNum(self):
        num=Num(config=self.the)
        prettyPrint = PrettyPrint()
        for i in range(1,1001):
            num.add(i, 0)
        prettyPrint.oo(num.nums())
        return self.the['nums']==len(num._has)
    
    """
    Method to test the.
    """
    def test_the(self):
        prettyPrint = PrettyPrint()
        prettyPrint.oo(self.the)
        return True
    
    """
    Method to test oo with complex json.
    """
    def test_oo(self):
        prettyPrint = PrettyPrint()
        result = prettyPrint.oo(self.the)
        return result == self.the