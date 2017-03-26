#!/usr/bin/env python3
# _*_ coding:utf8 _*_
import os
import time


logName = "/Users/db/Desktop/git/uplearning/py_sunday/demo/day7/a.txt"
speed = 100
size = os.path.getsize(logName)
deleteCnt = size // speed
with open(logName,'r+') as lfd:
    for n in range(deleteCnt):
        lfd.truncate(size - n * speed)
    kfd,truncate()
