#!/bin/env python3
# -*- coding:utf-8 -*-

# 导入SQLite驱动
import sqlite3

# 连接到SQLite数据库
conn = sqlite3.connect('test.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行sql语句
cursor.execute('CREATE TABLE user1 (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')
cursor.execute('INSERT INTO user1 (id, name) VALUES (\'1\', \'Michael\')')
cursor.execute('SELECT * FROM user1 WHERE id=?', ('1',))

# 通过rowcount获得插入的行数:
cursor.rowcount
# 获得查询结果
values = cursor.fetchall()  # 结果集是list,每个元素是tuple对应一行记录
cursor.close()
conn.close()


# example
# 出错情况下关闭connection对象和cursor对象
def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute('select name from user where score > %s AND score <= %s ORDER BY score' % (low, high))
        datas = cursor.fetchall()
        print(datas)
    finally:
        cursor.close()
        conn.close()
    return [x[0] for x in datas]


# another example
# 根据分数段查指定的名字
import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('CREATE TABLE user(id VARCHAR(20) PRIMARY KEY, name VARCHAR(20), score INT)')
cursor.execute(r"INSERT INTO user VALUES ('A-001', 'Adam', 95)")
cursor.execute(r"INSERT INTO user VALUES ('A-002', 'Bart', 62)")
cursor.execute(r"INSERT INTO user VALUES ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        # 执行查询语句:
        cursor.execute('SELECT * FROM user WHERE ?<= score AND score <=? ORDER BY score ASC', (low, high))
        # 获得查询结果集:
        values = cursor.fetchall()
    except Exception as e:
        print(e)
    else:
        print('conn is ok ')
    finally:
        cursor.close()  # 关闭游标
        conn.close()  # 关闭链接
    return [i[1] for i in values]  # 返回结果集中name的值


# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
