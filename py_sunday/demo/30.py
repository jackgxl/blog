# _*_ coding:utf8 _*_
n = int(raw_input("请输入一个数字: \n"))
m = str(n)
x = 0
for i in range(0,len(m)/2):
    if m[i] != m[-i-1]:
         x=1
         break
#        print "%d 不是回文数！！" % n
    else:
        x=2
#        print "%d 是回文数" % n
if x == 1:
    print "%d 不是回文数！！" % n
elif x ==2:
    print "%d 是回文数！！" % n
else:
    print "ERROR"
