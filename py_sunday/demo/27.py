# _*_ coding:utf8 _*_
l=[]
for i in range(1,6):
    s = raw_input("please input a character \n")
    l = l.append(s)
    print l
for j in range(0,len(l)+1,-1):
    print l[j]

