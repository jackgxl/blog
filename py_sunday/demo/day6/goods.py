# -*- coding:utf8 -*-
class Goods(object):
    @property
    def price(self):
        print("@property")
    @price.setter
    def price(self,value):
        print("@price.setter")
    @price.getter
    def price(self):
        print("@price.getter")
        print("end")
    @price.deleter
    def price(self):
        print("@price.deleter")
