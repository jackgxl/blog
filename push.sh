#!/bin/bash
cd /Users/db/Downloads/desktop_all/blog
git add *
git commit -m "`date +%F_%T`"
git push origin develop
git merge develop
