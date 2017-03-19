class A(object):
    @staticmethod
    def ex1():
        print("ex1")
        raise OSError("os error")

try:
    A.ex1()
    a=1
    a+=1
    print(a)
except Exception as ex:
    print(ex)
else:
    print("No error!")
