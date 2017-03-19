# -*-coding:utf8 -*-
class A:
    def __init__(self):
        print "A"


class B(A):
    def __init__(self):
        print "B"
        A.__init__(self)
        print "B"


b=B()
