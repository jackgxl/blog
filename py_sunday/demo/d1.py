# _*_ coding:utf8 _*_
for i in range(1,5):
    for j in range(1,5):
        for m in range(1,5):
            if (i != j) and (i != m) and (j != m):
                print i , j ,m
