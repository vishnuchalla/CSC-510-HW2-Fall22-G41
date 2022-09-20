from code.PrettyPrint import PrettyPrint
from code.Data import Data
from pprint import pp
from code.Num import Num

"""
Class to test data methods in the package.
"""
class TestData(object):
    """
    Method to load csv file into a Data
    """
    def test_data(self):
        d = Data('./data/auto93.csv')
        for col in d.cols.y.values():
            obj = {}
            for key, value in col.__dict__.items():
                if type(value) in [bool, int, float, str]:
                    obj[key] = value
            pretty_print = PrettyPrint()
            pretty_print.oo(obj)
        return True


    """
    Method to print some stats on columns
    """
    def test_stats(self):
        data = Data('data/auto93.csv')

        def div(col):
            return col.div()

        def mid(col):
            return col.mid()

        pretty_print = PrettyPrint()
        print("xmid", pretty_print.o(data.stats(2, data.cols.x, mid)))
        print("xdiv", pretty_print.o(data.stats(3, data.cols.x, div)))
        print("ymid", pretty_print.o(data.stats(2, data.cols.y, mid)))
        print("ydiv", pretty_print.o(data.stats(3, data.cols.y, div)))
    
        return True