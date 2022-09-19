import argparse
import csv as csvreader
from .Utils import Utils

"""
Formatter class for argument parser.
"""
class Formatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter): pass

"""
Class Csv to perform operations on a input csv file.
"""
class Csv:
    """
    Just a simple argument parser

    usage: Csv.py [-h] [-e EG] [-d DUMP] [-f FILE] [-n NUMS] [-s SEED] [-S SEPERATOR]

    CSV : summarized csv file
    (c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license

    options:
    -h, --help            show this help message and exit

    CSV parser:
    -e EG, --eg EG        start-up example (default: nothing)
    -d DUMP, --dump DUMP  on test failure, exit with stack dump (default: False)
    -f FILE, --file FILE  file with csv data (default: ../data/auto93.csv)
    -n NUMS, --nums NUMS  number of nums to keep (default: 512)
    -s SEED, --seed SEED  random number seed (default: 10019)
    -S SEPERATOR, --seperator SEPERATOR feild seperator (default: ,)
    """
    def __init__(self):
        parser_object = argparse.ArgumentParser(
            description="""CSV : summarized csv file\n(c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license""",
            formatter_class=Formatter,
        )

        parser = parser_object.add_argument_group("CSV parser")
        parser.add_argument("-e", "--eg", default="nothing", type=str, help="start-up example")
        parser.add_argument("-d", "--dump", default=False, type=bool, help="on test failure, exit with stack dump")
        parser.add_argument("-f", "--file", default="../data/auto93.csv", type=str, help="file with csv data")
        parser.add_argument("-n", "--nums", default=512, type=int, help="number of nums to keep")
        parser.add_argument("-s", "--seed", default=10019, type=int, help="random number seed")
        parser.add_argument("-S", "--seperator", default=",", type=str, help="feild seperator")

        self.args = parser_object.parse_args()
        print(self.args)

    """
    Method to read and process the csv rows.
    """
    def csv(self, fname, fun=None):
        pass
        sep = self.args.seperator
        with open(fname, newline='') as csvfile:
            reader = csvreader.reader(csvfile, delimiter=sep, quotechar='|')
            for row in reader:
                for idx in range(len(row)):
                    row[idx] = Utils().coerce(row[idx])
                fun(row)            