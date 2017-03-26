#!/usr/bin/env python3
# _*_ coding:utf8 _*_
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('child start...')
    time.sleep(20)
    print('child stop...')


def callback1(name):
    print("callback is called %s" % name)



if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(),callback=callback1)
    print('parant Working....')
    print('parant Working....')
    print('parant Working....')
    p.close()
    p.join()
    print('All subprocesses done.')
