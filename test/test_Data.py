from code.PrettyPrint import PrettyPrint
from code.Data import Data

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
                
    """
    Method to load csv file into a Data
    """
    def test_data(self):
        #d = Data('data/auto93.csv')
        for _,col in (d.cols.y.items()):
            prettyPrint = PrettyPrint()
            prettyPrint.oo(col)
        
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

        prettyPrint=PrettyPrint()
        print("xmid",prettyPrint.o(data.stats(2,data.cols.x,mid)))
        print("xdiv",prettyPrint.o(data.stats(3,data.cols.x,div)))
        print("ymid",prettyPrint.o(data.stats(2,data.cols.y,mid)))
        print("ydiv",prettyPrint.o(data.stats(3,data.cols.y,div)))
    
        return True