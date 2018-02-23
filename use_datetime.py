#!/bin/env python3
# -*- coding:utf-8 -*-

from datetime import datetime

# 获取当前datetime
now = datetime.now()
print(now)

# 获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20)
print(dt)

# 把datetime转换为timestamp
print(dt.timestamp())

# 把timestamp转换为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))  # 本地时间
print(datetime.utcfromtimestamp(t))  # UTC时间

# datetime 转换为str
now = datetime.now()
print(now.strftime('%a,%b %d %H %M'))

# datetime加减
from datetime import timedelta
now = datetime.now()
print(
    now,
    now + timedelta(hours=10),  # 后10H
    now - timedelta(days=1),  # 昨天
    now + timedelta(days=3, hours=3)  # 后3天3小时候后
)

# 本地时间转换为UTC时间
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now=datetime.now()      # 当前系统时间
print(now)
dt=now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt)

# 时区转换
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)



def to_timestamp(dt_str, tz_str):
    # 创建指定时间的datetime对象
    temp = dt.strptime(dt_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=tz(td(hours=int(tz_str[3:5]))))
    # 转换为UTC时间
    nt_dt = temp.astimezone(tz.utc)

    return nt_dt.timestamp()