i,j=0,0
for i in range(1,100//4+1):
    for j in range(1,100//6+1):
        if 4*i + 6*j == 100:
            print(i,j)
