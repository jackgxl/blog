# _*_ coding:utf8 _*_
score = int(raw_input('input score: \n'))
if score > 90 :
    grade = 'A'
elif score >=60 :
    grade = 'B'
else:
    grade = 'C'
print "%d belogs to %s" % (score,grade)
