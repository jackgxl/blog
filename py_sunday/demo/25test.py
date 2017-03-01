# _*_ coding:utf8 _*_
#a = int(raw_input("请输入一个整数: \n"))
def f1(a):
    if a == 1:
        return 1
    else:
        return a*f1(a-1)
sum = 0
for b in range(1,21):
    sum = sum + f1(b)
print sum
