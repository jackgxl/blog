# _*_ coding:utf8 _*_

from multiprocessing import Process
import os
import time

def run_proc(name):
    print('run child process %s (%s) ...' % (name,os.getpid()))
    time.sleep(10)

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('child process will start.')
    p.start()
    p.join()
    print('Child processs end.')
