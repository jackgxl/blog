# -*- coding:utf8 -*-

import sys

@staticmethod
def add(a,b):
    a= a+1
    b = b+1
    print(a,b)
def _checkArgs():
    if len(sys.argv) <= 2:
        print("ERROR")
        sys.exit(0)
if __name__=="__main__":
    _checkArgs()
    print("para pass.")
    #add
    A.add()
    sys.exit(0)
