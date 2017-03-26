#!/usr/bin/env python3
# -*- coding:utf8 -*-

confFile=""
tmpResult = []
with open(confFile,'r+') as fd:
    for line in fd.readlines():
        if line != "\n":
            key = line.split("=")[0].strip()
                tmpResult.append(key + "=" + "vvvvvv" + "\n")
    fd.seek(0)
    fd.truncate()
    for i in tmpResult:
        fd.write(i)
    fd.flush()
