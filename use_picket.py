#!/bin/env pyton3
# -*- coding:utf-8 -*-

d=dict(name='Bob',age=20,score=88)

#变量从内存中编程可存储或传输的过程，序列化pickling
#把变量内容从序列化的对象重新读到内存中，反序列化unpicking

import pickle

# dumps()方法任意对象序列化成bytes
d1=dict(name='Bob',age=20,score=88)
print(pickle.dumps(d))
# dump()方法把对象序列化后写入file-like Object
try:
    f=open(r'E:/Material/2-Development/Python/Python code/learn-python3/dump.txt','wb')
    pickle.dump(d,f)
    f.close()

#loads()方法 反序列化除对象
    f=open(r'E:/Material/2-Development/Python/Python code/learn-python3/dump.txt','rb')
    d=pickle.load(f)    # or pickle.loads(f)
    f.close()
    print(d)




except Exception as e:
    print(e)


