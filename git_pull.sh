#!/bin/bash
git add *
git commit -m "`date +%F_%T`"
git push origin develop
git merge master
