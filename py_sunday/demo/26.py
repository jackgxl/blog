# _*_ coding:utf8 _*_
def func(n):
    if n==1:
        return 1
    else :
        return n*func(n-1)
for i in range(1,6):
    m = func(i)
    print "%d! = %d "   % (i,m)
