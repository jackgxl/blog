# -*- coding:utf8 -*-
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

bart = Student('BJ',90)
print(bart.name)
