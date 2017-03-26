import json
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
                'name':std.name,
                'age':std.age,
                'score':std.score
                }
s = Student('bob',20,88)
print(json.dumps(s,student2dict(s)))
