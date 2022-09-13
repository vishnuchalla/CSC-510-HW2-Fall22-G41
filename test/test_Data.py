import csv   
from code.PrettyPrint import PrettyPrint

"""
Class to test data methods in the package.
"""
class TestData(object):
    
    """
    Method to read the csv file
    """
    def test_readcsv(self):
        n=0
        with open('data/auto93.csv', 'r') as file:
            my_reader = csv.reader(file)
            for row in my_reader:
                print(row)
                n+=1
                if n > 10:
                    return
                else:
                    prettyPrint = PrettyPrint()
                    prettyPrint.oo(row)
        return True