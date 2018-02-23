#!/bin/env python3
# -*- coding:utf-8 -*-

# 枚举类型定义一个class类型，枚举类型定义一个class类型
# Enum类

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique  # 确保没有重复值
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon

# 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量
print(
    day1,
    Weekday.Thu,
    Weekday['Tue'],
    Weekday.Thu.value,
    day1 == Weekday.Mon,
    Weekday(6)
)
