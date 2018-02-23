#!/bin/env python3
# -*- coding:utf-8 -*-


# try内代码块出错时，后续语句不会被执行，执行except捕获，反之相反
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')


# except捕获多个的错误
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')


# except捕获没有错误执行else语句
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

# 所有的错误类型都继承自BaseException，父类可捕获子类错误，跨越多层捕获错误
try:
    foo(s)
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')