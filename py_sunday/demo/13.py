# _*_ coding:utf8 _*_
for n in range(100,1000):
    i = n/100
    j = n/10%10
    m = n%10
    if n == i**3 + j ** 3 + m ** 3:
        print n
