with open('/Users/db/Desktop/git/uplearning/py_sunday/demo/day7/test.conf','r') as fd:
    while True:
        line = fd.readline()
        if line != '':
            print(line.strip())
        else:
            break
