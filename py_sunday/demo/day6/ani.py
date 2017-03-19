# -*- coding:utf8 -*-
class Animal(object):
    def __init__(self,name):
        self.name = name
    def greet(self):
        print("hello I am %s" % self.name)

class Dog(Animal):
    def greet(self):
        super(Dog,self).greet()
        #super().greet()
        print("wang wang ...")

ani = Animal("trump")
ani.greet()

d = Dog("obama")
d.greet()
print(Dog.mro())
