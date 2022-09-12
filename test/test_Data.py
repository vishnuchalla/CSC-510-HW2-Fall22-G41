from code.PrettyPrint import PrettyPrint
from code.ReadFile import ReadFile
from code.Row import Row

"""
Class to test data methods in the package.
"""
class TestData(object):

    def test_readcsv(self):
        csv_data = ReadFile()
        prettyPrint = PrettyPrint()
        n=0
        def row_func(self):
            row=Row()
            n+=1
            if n>10:
                return
            else:
                prettyPrint.oo(row)

        csv = csv_data.csv('data/auto93.csv',row_func)
        return True