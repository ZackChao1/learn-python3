#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


def person(name, age, **kw):    # 关键参数组装dict
    print('name:', name, 'age:', age, 'other:', kw)


print(person('Michael',30,city='Bjeijing'))
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('zzc', 31, **extra))


def print_scores(**kw1):  # 关键字参数,内部自动组装dict
    print('		Name Score')
    print('----------------')
    for name, score in kw1.items():
        print('%10s	%d' % (name, score))
    print('----------------')


print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}
print_scores(**data)  # 关键参数接收dict


def print_info(name, *, gender, city='Beijing', age):   #命名关键字参数,dict
    print('Personal Info')
    print('-------------')
    print('	Name:%s' % name)
    print('Gender:%s' % gender)
    print('	City:%s' % city)
    print('	Age:%s' % age)
    print()


print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)
print_info('zzc',1,2,3,gender='xxx',city='xxx',age=11)
