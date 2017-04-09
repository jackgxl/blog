# -*- coding:utf8 -*-

import configparser

cf = configparser.ConfigParser()
cf.read("test.conf")
opts = cf.sections()
print('sections:',opts)
