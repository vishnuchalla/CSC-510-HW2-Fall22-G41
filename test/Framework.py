from subprocess import list2cmdline
import sys
import os
from unittest.result import failfast

sys.path.insert(1, os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

class FrameWork:
    def __init__(self, testMethods):
        self.testMethods = testMethods
        self.fails = 0

    def list(self):
        self.testMethods.sort()
    
    def ls(self):
        for eachMethod in self.testMethods:
            className, testMethod = eachMethod.split('.')
            print(className[:-2] + ':' + testMethod[:-2])
    
    def all(self):
        for eachMethod in self.testMethods:
            className, testMethod = eachMethod.split('.')
            result = eval(eachMethod)
            msg, exit_code = ("PASSED", 0) if (result) else ("FAILED", 1)
            self.fails += exit_code
            print(className[:-2] + ':' + testMethod[:-2] + " - " + msg)

if __name__ == '__main__':
    testFiles = [filename.split('.')[0] for filename in os.listdir(os.getcwd()) if filename.startswith("test")]
    testMethods = []
    for eachFile in testFiles:
        first, second = eachFile.split('_')
        first = first[0].upper() + first[1:]
        className = first + second
        eval("exec('from test.' + eachFile + ' import ' + className)")
        testMethods += [className+'().'+func+'()' for func in dir(eval(className)) if callable(getattr(eval(className), func)) and not func.startswith("__")]
    frameWork = FrameWork(testMethods)
    frameWork.all()
    print("--------------Summary--------------")
    totalTests = len(frameWork.testMethods)
    failures = frameWork.fails
    print(str(totalTests - failures) + " PASSED ", end="\t\t")
    print(str(failures) + " FAILED ")
    print("Success Rate:- " + str(((totalTests - failures)*100)/totalTests) + "%", end="\t\t")
    print("Failure Rate:- " + str((failures*100)/totalTests) + "%")
    sys.exit(failures)