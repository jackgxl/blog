# _*_ coding:utf8 _*_
import os
conf_file = "/Users/db/Desktop/git/uplearning/py_sunday/demo/day7/test.conf"
if not os.path.exists(conf_file):
    quit(1)



with open(conf_file,'r') as f:
    listIterms = f.readlines()



for item in listIterms:
    l= item.split("=")
#    print(l)
    if l[0] != '/n':
        print(l)
        result[l[0]] = l[1].strip()
    else:
        pass
print(result)
