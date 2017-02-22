# _*_ coding:utf8 _*_
def fib(n):
    f = [0,1]
    if n == 1:
        return [0]
    if n == 2:
        return f
    for i in range(2,n):
        f.append(f[-1]+f[-2])
    return f
print fib(2)
print fib(1)
print fib(4)
print fib(30)
