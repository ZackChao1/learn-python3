#!/bin/env python3
# -*- coding:utf-8 -*-


# another sql driver
# pymysql

import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='a5230411', db='test')
cur = conn.cursor()
cur.execute("SELECT * FROM users")
for r in cur.fetchall():        # 取结果集
    print(r)
    # cur.close()
conn.close()

