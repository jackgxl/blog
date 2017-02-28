# _*_ coding:utf8 _*_
s = raw_input("输入一个字符串： \n")
#s = 'abcde'
n = len(s)
print n
l = list(s)
for i in range(0,len(l)):
    print l.pop()
