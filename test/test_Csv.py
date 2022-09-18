from code.PrettyPrint import PrettyPrint
from code.Csv import Csv
from code.Utils import Utils

"""
Class to test Csv methods in the package.
"""
class TestCsv(object):
        
    """
    Method to test csv functionality.
    Sample Test Input: Its our csv file.
    Sample Test Output:
    {Clndrs Volume Hp: Lbs- Acc+ Model origin Mpg+}
    {8 304.0 193 4732 18.5 70 1 10}
    {8 360 215 4615 14 70 1 10}
    {8 307 200 4376 15 70 1 10}
    {8 318 210 4382 13.5 70 1 10}
    {8 429 208 4633 11 72 1 10}
    {8 400 150 4997 14 73 1 10}
    {8 350 180 3664 11 73 1 10}
    {8 383 180 4955 11.5 71 1 10}
    {8 350 160 4456 13.5 72 1 10}
    TestCsv:test_csv - PASSED
    """
    def test_csv(self):
        csv = Csv()
        csv.csv("./data/auto93.csv", Utils().log)
        return True