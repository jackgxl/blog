# _*_ coding:utf8 _*_

a=2.0
b=1.0
l = []
for n in range(1,21):
    b,a=a,a+b
    l.append(a / b)
print reduce(lambda x,y: x+y ,l)
