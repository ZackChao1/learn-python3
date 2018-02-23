#!/bin/env python3
# -*- conding:utf-8 -*-


# dict对象序列化为xml or json
# dumps()方法，转为json str
# dump()方法，写入file-like Object,python object
import json

d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))  # retrun json str

# json反序列化为dict对象
# loads()方法，json字符串反序列化
# load()方法，file-like Object读取字符串并反序列化
json_str = '{"age":20,"score":88,"name":"Bob"}'
json.loads(json_str)  # retrun dict


# 序列化和反序列化类
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

# Student实例转换为dict
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

# dict 转换为student实例
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

# 任意class的实例变为dict
print(json.dumps(s, default=lambda obj: obj.__dict__))
