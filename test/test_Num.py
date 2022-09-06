import sys
import os
from typing import OrderedDict
sys.path.insert(1, os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
from code.Num import Num
import inspect

"""
Class to test Num.
"""

class TestNum(object):
    """
    Method to test per method.
    """
    def test_per(self):
        num = Num()
        result = num.per([1,2,3,4,5], 0.5)
        return result == 4

    """
    Method to test the nums method with sorted flag set to False.
    """
    def test_nums_false_case(self):
        num = Num()
        num.isSorted = False
        num._has = {1: 3, 2: 4}
        result = num.nums()
        return result == OrderedDict({1:3, 2:4}) and num.isSorted == True
    
    """
    Method to test the nums method with sorted flag set to True.
    """
    def test_nums_true_case(self):
        num = Num()
        num.isSorted = True
        result = num.nums()
        return result == {} and num.isSorted == True

    """
    Method to test the div method.
    """
    def test_div(self):
        num = Num()
        num.isSorted = False
        num._has = {1: 3, 2: 4}
        result = num.div([1,2,3,4,5])
        return round(result, 2) == 0.39

    """
    Method to test the mid method.
    """
    def test_mid(self):
        num = Num()
        num.isSorted = False
        num._has = {1: 3, 2: 4, 3: 5}
        result = num.mid()
        return result == 4