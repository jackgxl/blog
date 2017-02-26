# _*_ coding:utf8 _*_
from sys import stdout
for i in range(4):
    for j in range(2-i+1):
        stdout.write(' ')
    for k in range(2*i+1):
        stdout.write('*')
    print
