from typing import OrderedDict
from code.Num import Num
import Framework

"""
Class to test Num.
"""

class TestNum(object):

    """
    Init method to get the command line args.
    """
    def __init__(self):
        self.the = Framework.updated_the

    """
    Method to test per method.
    """
    def test_per(self):
        num = Num(config=self.the)
        result = num.per({1:1, 2:2, 3:3, 4:4, 5:5}, 0.5)
        return result == 3

    """
    Method to test the nums method with sorted flag set to False.
    """
    def test_nums_false_case(self):
        num = Num(config=self.the)
        num.isSorted = False
        num._has = {1: 3, 2: 4}
        result = num.nums()
        return result == OrderedDict({1:3, 2:4}) and num.isSorted == True
    
    """
    Method to test the nums method with sorted flag set to True.
    """
    def test_nums_true_case(self):
        num = Num(config=self.the)
        num.isSorted = True
        result = num.nums()
        return result == {} and num.isSorted == True

    """
    Method to test the div method.
    """
    def test_div(self):
        num = Num(config=self.the)
        num.isSorted = False
        num._has = {1: 3, 2: 4}
        result = num.div([1,2,3,4,5])
        return round(result, 2) == 0.39

    """
    Method to test the mid method.
    """
    def test_mid(self):
        num = Num(config=self.the)
        num.isSorted = False
        num._has = {1: 3, 2: 4, 3: 5}
        result = num.mid()
        return result == 4
    
    """
    Method to test the add method for if block.
    """
    def test_add_if_block(self):
        num = Num(config=self.the)
        num._has = {1: 3, 2: 4, 3: 5}
        num.add(6, 6)
        return num._has == {1: 3, 2: 4, 3: 5, 4: 6}
    
    """
    Method to test the add method for elifblock.
    """
    def test_add_elifblock(self):
        num = Num(config=self.the)
        num._has = {1: 3, 2: 4, 3: 5}
        num.add(6, 6)
        return len(num._has) == 4
    
    """
    Method to test num method: The middle and diversity of a set of numbers is called "median"
    and "standard deviation" (and the latter is zero when all the nums are the same).
    """
    def test_num(self):
        num=Num(config=self.the)
        for i in range(1,101):
            num.add(i,0)
        mid,div = num.mid(), num.div(a=None)
        print(mid,div)
        return 50<=mid and mid<=52 and 30.5<div and div<32 and 100==len(num._has)