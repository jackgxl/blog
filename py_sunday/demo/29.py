# _*_ coding:utf8 _*_
n = int(raw_input("请输入一个五位数: \n"))
a = n/10000
b = n%10000 / 1000
c = n%1000 / 100
d = n%100 / 10
e = n%10 
if a != 0:
    print "五位数：" ,a,b,c,d,e
elif b != 0:
    print "四位数： ",b,c,d,e
elif c != 0 : 
    print "三位数：", c,d,e
elif d != 0 :
    print "二位数：",d,e
else :
    print "一位数：",e
