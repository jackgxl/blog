# _*_ coding:utf8 _*_
def output(s,l):
    if l == 0:
        return 0
    print (s[l-1])
    output(s,l-1)

s = raw_input('Input a string: \n')
l = len(s)
output(s,l)
