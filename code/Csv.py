import csv as csvreader
from code.Utils import Utils

"""
Class Csv to perform operations on a input csv file.
"""
class Csv:
    """
    Method to read and process the csv rows.
    """

    def csv(self, fname, sep=",", fun=None):
        with open(fname, newline='') as csvfile:
            reader = csvreader.reader(csvfile, delimiter=sep, quotechar='|')
            for row in reader:
                for idx in range(len(row)):
                    row[idx] = Utils().coerce(row[idx])
                fun(row)
