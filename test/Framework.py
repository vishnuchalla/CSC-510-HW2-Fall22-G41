import sys
import os
import re
import traceback

sys.path.insert(0, os.path.abspath(os.getcwd()))
from code.Utils import Utils

help='''
    CSV : summarized csv file
    USAGE: python test.py [OPTIONS]
    OPTIONS:
    -e  --eg        start-up example                      = nothing
    -d  --dump      on test failure, exit with stack dump = false
    -f  --file      file with csv data                    = ../data/auto93.csv
    -h  --help      show help                             = false
    -n  --nums      number of nums to keep                = 512
    -s  --seed      random number seed                    = 10019
    -S  --seperator feild seperator                       = ,
'''

the = dict()

def default_the():
    eachLine = help.split('\n')
    parse = False
    for line  in eachLine:
        if 'OPTIONS:' in line:
            parse = True
            continue
        if parse:
            each = re.sub(' +', ' ', line.strip())
            if each != '':
                vars = each.split(' = ')
                the[vars[0].split(' ')[1][2:]] = vars[1]
    return the

the = default_the()

def cli(t):
    args = {idx: eachArg for idx, eachArg in enumerate(sys.argv)}
    for slot,v in t.items():
        v = str(v)
        for n,x in args.items():
            if ((x == '-' + slot[0:1]) or (x == '--' + slot)):
                v = 'true' if (v=='false') else 'false' if (v=='true') else args[n+1]
        t[slot] = Utils().coerce(v)
    if t['help']:
        print(help)
        sys.exit(0)
    return t

updated_the = cli(the)

class FrameWork:
    def __init__(self, testMethods):
        self.testMethods = testMethods
        self.fails = 0

    def list(self):
        self.testMethods.sort()
    
    def ls(self):
        print("-----------------------------------")
        for eachMethod in self.testMethods:
            className, testMethod = eachMethod.split('.')
            print(className[:-2] + ':' + testMethod[:-2])
        print("-----------------------------------")
    
    def all(self):
        for eachMethod in self.testMethods:
            className, testMethod = eachMethod.split('.')
            try:
                print("-----------------------------------")
                result = eval(eachMethod)
            except Exception as e:
                print("CRASH in testCase: " + str(eachMethod) + ". Error cause: " + str(e))
                self.fails += 1
                print("The entire stack trace here: ")
                traceback.print_exc()
            msg, exit_code = ("PASSED", 0) if (result) else ("FAILED", 1)
            self.fails += exit_code
            print(className[:-2] + ':' + testMethod[:-2] + " - " + msg)
            print("-----------------------------------")

if __name__ == '__main__':
    print(updated_the)
    if(updated_the['eg'] != "nothing"):
        testFiles = [filename.split('.')[0] for filename in os.listdir(os.getcwd()+"/test") if filename.startswith("test")]
        testMethods = []
        for eachFile in testFiles:
            first, second = eachFile.split('_')
            first = first[0].upper() + first[1:]
            className = first + second
            eval("exec('from test.' + eachFile + ' import ' + className)")
            testMethods += [className+'().'+func+'()' for func in dir(eval(className)) if callable(getattr(eval(className), func)) and not func.startswith("__")]
        if(updated_the['eg'] == "LS"):
            FrameWork(testMethods).ls()
            sys.exit(0)
        elif(updated_the['eg'].lower() in ["bignum", "csv", "data", "num", "stats", "sym", "the"]):
            pattern = updated_the['eg']
            testMethods = [each for each in testMethods if (re.search(pattern.lower(), each.lower()) is not None)]
        elif(updated_the['eg'] != "ALL"):
            print("Invalid Test Input, Below are the valid tests")
            print(str(["ALL", "LS", "bignum", "csv", "data", "num", "stats", "sym", "the"]))
            sys.exit(0)
        frameWork = FrameWork(testMethods)
        frameWork.ls()
        frameWork.all()
        print("--------------Summary--------------")
        totalTests = len(frameWork.testMethods)
        failures = frameWork.fails
        print(str(totalTests - failures) + " PASSED ", end="\t\t")
        print(str(failures) + " FAILED ")
        print("Success Rate:- " + str(((totalTests - failures)*100)/totalTests) + "%", end="\t\t")
        print("Failure Rate:- " + str((failures*100)/totalTests) + "%")
        sys.exit(failures)
    else:
        sys.exit(0)
