#!/bin/env python3
# -*- encoding:utf-8 -*-





from datetime import datetime
import os



# os 常用操作
print(os.name,'\n',
      #os.uname(),'\n', # windows上不提供该方法
      os.environ,'\n',
      os.environ.get('PATH'),'\n',
      os.path.abspath('.'),'\n',
      os.path.join('/a/b/c','testdir'),'\n',
      os.mkdir(r'd:\testdir'),'\n',
      os.rmdir(r'd:\testdir'),'\n',
      os.path.split('/Users/michael/testdir/file.txt'),'\n',    #split dirname and filename
      os.path.splitext('/Users/michael/testdir/file.txt'),'\n', #split path and extendname
    #  os.rename('test.txt','text.py'),'\n',
    #  os.remove('text.py')
      )










# dir -l
pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))






def searchfile(name='zzc', path='e:/'):
    os.chdir(path)
    listall = os.listdir(path)
    try:
        for x in listall:
            join_path = os.path.join(path, x)
            if os.path.isfile(join_path) and name in os.path.basename(join_path) :
                print(os.path.dirname(join_path), os.path.basename(join_path))
            elif os.path.isdir(join_path) :
                searchfile(name, join_path)
    except PermissionError as e:
        print('except',e)

searchfile('360.119862FE39E780D0C56719FB545E9E20.q3q')
