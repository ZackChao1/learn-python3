#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/3/2018 9:12 AM
# @Author  : Aries
# @Site    : 
# @File    : example1~10.py
# @Software: Pychrm


'''
programe example 100
'''

'''
题目1：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
程序分析：
    可填在百位、十位、个位的数字都是1、2、3、4;   # range(1,5)
    组成所有的排列后再去掉不满足条件的排列。      # if 判断
'''
# 程序源码
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k) and (i != j) and (j != k):
                print(i, j, k)

'''
题目2：企业发放的奖金根据利润提成。# int bonus 
    利润(I)低于或等于10万元时，奖金可提10%；    # input I
    利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；
    20万到40万之间时，高于20万元的部分，可提成5%；
    40万到60万之间时高于40万元的部分，可提成3%；
    60万到100万之间时，高于60万元的部分，可提成1.5%，
    高于100万元时，超过100万元的部分按1%提成，   # if 判断不同范围
    从键盘输入当月利润I，求应发放奖金总数？
程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。　 
'''
# 程序源码
# 低于部分的利润提成
bonus1 = 100000 * 0.1
bonus2 = bonus1 + 100000 * 0.500075
bonus4 = bonus2 + 200000 * 0.5
bonus6 = bonus4 + 200000 * 0.3
bonus10 = bonus6 + 400000 * 0.15

i = int(input('input gain:\n'))
if i <= 100000:
    bonus = i * 0.1
elif i <= 200000:
    bonus = bonus1 + (i - 100000) * 0.075  # 低于部分和高于部分
elif i <= 400000:
    bonus = bonus2 + (i - 200000) * 0.05
elif i <= 600000:
    bonus = bonus4 + (i - 400000) * 0.03
elif i <= 100000:
    bonus = bonus6 + (i - 600000) * 0.015
else:
    bonus = bonus10 + (i - 100000) * 0.01
print('bonus', bonus)

'''
题目3：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
程序分析：在10万以内判断，先将该数加上100后再开方，再将该数加上268后再开方，
        如果开方后的结果满足如下条件
        完全数：一个数的平方根等于该数。
        ，即是结果。
'''
# 程序源码
import math

for i in range(10000):
    x = math.sqrt(i + 100)  # 假设完全数x
    y = math.sqrt(i + 268)  # 假设完全数y
    if (x * x == i + 100) and (y * y == i + 268):  # 判断完全数
        print(i)

'''
题目4：输入某年某月某日，判断这一天是这一年的第几天？ # 年月日 input() 月数总天数集合
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊 
     情况，闰年且输入月份大于3时需考虑多加一天。 
'''
# 程序源码

year = int(input('year:\n'))  # 注意转换为int类型
month = int(input('month:\n'))
day = int(input('day：\n'))
sum=0
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)  # 第几个月的总天数
if 0 <= month <= 12:
    sum = months[month - 1] # 计算前几个月

else:
    print('data error')
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):    # 判断闰年多加一天
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print('it is the %dth day.' % sum)


'''
题目5：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换,
        然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。 
'''
# 程序源码
l=[]
for i in range(3):  # 输入x, y,z
    x=int(input('integer:\n'))
    l.append(x)
l.sort()    # 排序 默认小到大
print(l)

'''
题目6：用*号输出字母C的图案。
程序分析：可先用’*’号在纸上写出字母C，再分行输出。 
'''
# 程序源码
print('Hello Python world!\n')
print('*'*10)
for i in range(5):
    print('*        *')
print('*\n'*6)      # 注意换行
print('*'*10)


'''
题目7：输出特殊图案
'''
# 程序源码:

a=176;b=219
print(chr(b),chr(a),chr(a),chr(a),chr(b))
print(chr(a),chr(b),chr(a),chr(b),chr(a))
print(chr(a),chr(a),chr(b),chr(a),chr(a))
print(chr(a),chr(b),chr(a),chr(b),chr(a))
print(chr(b),chr(a),chr(a),chr(a),chr(b))

'''
题目8：输出9*9口诀
程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
'''
# 程序源码：
for i in range(1,10):
    for j in range(1,10):
        result=i*j
        print('%d * %d = %-3d'%(i,j,result))  # -3d表示左对齐，占3位
    print('\n')  # 每一行后换行


'''
题目9：输出国际象棋棋盘
程序分析：用i控制行，j来控制列，根据i+j的和的变化来控制输出黑方格，还是白方格。。
'''
# 程序源码：
import sys
for i in range(8):
    for j in range(8):
        if(i + j) % 2 == 0:     # i+j 控制控制黑白
            sys.stdout.write(chr(219))
            sys.stdout.write(chr(219))
        else:
            sys.stdout.write(' ')
    print('')

'''
题目10：打印楼梯，同时在楼梯上方打印两个笑脸。
程序分析：用i控制行，j来控制列，根据i+j的和的变化来控制输出黑方格，还是白方格。。
'''
# 程序源码：
sys.stdout.write(chr(1))
sys.stdout.write(chr(1))
print(' ')  # 头一行
for i in range(1,11):
    for j in range(1,j):
        sys.stdout.write(chr(219))
        sys.stdout.write(chr(219))
    print(' ')  # 行间空格