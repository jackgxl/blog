with open('/Users/db/Desktop/git/uplearning/py_sunday/demo/day7/test.conf','r') as fd:
    while True:
        c = fd.read(5)
        if c != '':
            print(c)
        else:
            break
