#day 2

###ord()

```
    函数获取字符的整数表示
```

###chr()

```
    函数把编码 转换为对应的字符   
```

###list
3种构造方法
list=list()
list=[1,2,3,'a']
list=list((1,2,4,))


###str
help(str)
dir(ste)
###int
help(int)
###tuple
help(tuple)

t=(1,)

t=(1,[2,3],'a','b')
###set
help(set)
###函数
```
def checkEmail:
    if email is None or not isinstance(email,str):
        print("None or no str")
        retrun
    if email.find("@") == -1:
        print("no @")
        return
    if email.count("@")>1:
        print("more than 1 @")
        return
    if email[0] == "@" or email[-1] =="@":
        print("@head or tail")
        return
    if len(email)>=20:
        print("len over 20")
        retrun
    if not email.endswith(".com") and not email.endswith(".cn"):
        print("ERROR:not .com .cn")
        return
    '''
    if not email.endswith(".com"):
        print("ERROR:not .com")
        return
    elif not email.endswith(".cn"):
        print("ERROR:not .cn")
        return
    '''
    (username,domain) = email.split("@")
    retrun(username,domain)
```