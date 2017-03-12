# -*- coding:utf8 -*-
class Animal(object):
    def __init__(self,name,age,Type):
        self._name = name
        self._age = age
        self._Type = Type
#    def printAll(self):
#        print('ani name is %s,age is %d,leibie is %s !! \n ' % (self.name,self.age,self.leibie))
    def getName(self):
        return self._name
    def getAge(self):
        return self._age
    def getType(self):
        return self._Type
