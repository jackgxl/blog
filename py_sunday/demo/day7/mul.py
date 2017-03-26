#!/usr/bin/env python3
# _*_ coding:utf8 _*_
import os
import time
print('Process (%s) start ...'  % os.getpid())

pid = os.fork()
if pid == 0 :
    print('I am child process (%s) and my parent is %s.'  % (os.getpid(),os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(),pid))

time.sleep(6)
pid2 = os.fork()
time.sleep(10)
print("end")
