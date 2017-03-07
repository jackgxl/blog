# _*_ coding:utf8 _*_
n = int(raw_input("5 weishu : \n"))
a = n/10000
b = n%10000 / 1000
c = n%1000 / 100
d = n%100 / 10
e = n%10
if a != 0 :
    print "5: ",a,b,c,d,e
elif b != 0:
    print "4: ",b,c,d,e
elif c != 0:
    print "3: ",c,d,e
elif d != 0:
    print "2: ",d,e
else:
    print "1: ",e
