#!/bin/env python3
# -*- coding:utf-8 -*-


# 出错抛异常栈
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('0')


main()

# Traceback (most recent call last):    # 错误的跟踪信息
#   File "err.py", line 11, in <module>
#     main()                            # 调用main()出错了，在代码文件err.py的第11行代码，但原因是第9行
#   File "err.py", line 9, in main
#     bar('0')                          # 调用bar('0')出错了，在代码文件err.py的第9行代码，但原因是第6行：
#   File "err.py", line 6, in bar
#     return foo(s) * 2                 # return foo(s) * 2这个语句出错了
#   File "err.py", line 3, in foo
#     return 10 / int(s)                # return foo(s) * 2这个语句出错了
# ZeroDivisionError: division by zero   # 错误产生的源头
