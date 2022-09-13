from code.Csv import Csv

"""
Class to test data methods in the package.
"""
class TestData(object):
    
    """
    Method to read the csv file
    """
    def test_readcsv(self):
        n=0
        csv=Csv()
        prettyPrint = PrettyPrint()
        my_reader = csv.csv('data/auto93.csv',fun=None,sep=None,src=None,s=None,t=None)
        for row in my_reader:
            print(row)
            n+=1
            if n > 10:
                return
            else:
                prettyPrint.oo(row)
        return True