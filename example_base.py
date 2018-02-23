# 质数
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print('%d 等于 %d*%d' % (num, i, j))
            break
    else:
        print(num, '是个质数')

num = []
i = 2
for i in range(2, 100):
    j = 2
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        num.append(i)
print(num)

# 素数
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j += 1
        if (j > i / j): print(i, '是素数')
    i += 1
print('Bye!')  # 注意：循环内输出是输出多条，循环外输出只显示循环最终一条；

# *字塔
i = 1
while i <= 9:
    if i < 5:  # 判断条件1
        print("*" * i)
    elif i < 9:
        j = i - 2 * (i - 5)
        print('*' * j)
    i += 1
else:
    print('*')

# 冒泡排序# 定义列表 list
arays = [1, 8, 2, 6, 3, 9, 4]
for i in range(len(arays)):
    for j in range(i + 1):
        if arays[i] < arays[j]:
            # 实现连个变量的互换
            arays[i], arays[j] = arays[j], arays[i]
print(arays)

# 二维列表
list_2d = [[0 for i in range(5)] for i in range(5)]
list_2d[0].append(3)
list_2d[0].append(4)
list_2d[0].append(99)
print(list_2d)
list_2d.pop(0)

# 格式化日期
import time
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

#datetime
import datetime
i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)

# 实现反转函数reverse
def reverse(li):
    for i in range(0, len(li)/2):
        temp = li[i]    # 临时存入前半部分
        li[i] = li[-i-1]    # 尾部
        li[-i-1] = temp     # 首部
def reverse(ListInput):
    RevList=[]
    for i in range (len(ListInput)):
        RevList.append(ListInput.pop())     # 取出最后一个元素放入新列表，旧列表删除该元素mo
    return RevList