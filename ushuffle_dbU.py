#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/16/2018 3:12 PM
# @Author  : Aries
# @Site    : 
# @File    : ushuffle_dbU.py
# @Software: PyCharm


from distutils.log import warn as printf
import os
from random import randrange as rand

if isinstance(__builtins__,dict) and 'raw_input' in __builtins__:
    scanf=raw_input
elif hasattr(__builtins__,'raw_input'):         # hasattr()
    scanf=raw_input
else:
    scanf=input





COLSIZ=10
FIELDS=('login','userid','progid')
RDBMSs={'s':'sqlite','m':'mysql','g':'gadfly'}
DBNAME='test'
DBUSER='root'
DB_EXC=None
NAMELEN=16


tformat=lambda s:str(s).title().ljust(COLSIZ)   # ljust() 宽度左对齐 title() 头大写 str()
cformat=lambda s:s.opper().ljust(COLSIZ)    # opper() 全大写



def setup() -> object:
    return RDBMSs[input('''
Choose a database system:
    (M)ySQL
    (G)adfly
    (S)QLite
Enter choice:''').strip().lower()[0]]   # strip() lower()

def connect(db,DBNAME):
    global DB_EXC   # Database Exception Type
    dbDir='%s_%s' % (db,DBNAME)     #  dbdir

    if db=='sqlite':
        try:
            import sqlite3
        except ImportError:
            try:
                from pysqlite2 import  dbapi2 as sqlite3
            except ImportError:
                return None
        DB_EXC=sqlite3
        if not os.path.isdir(dbDir):
            os.mkdir(dbDir)
        cxn=sqlite.connect(os.path.join(dbDir,DBNAME))

    elif db=='mysql':
        try:
            import MySQLdb
            import _mysql_exceptions as DB_EXC

            try:
                    cxn=MySQLdb.connect(db=DBNAME)
            except DB_EXC.OperationalError:
                try:
                    cxn=MySQLdb.connect(user=DBUSER)
                    cxn.query('create database %s' % DBNAME)
                    cxn.commit()
                    cxn.close()
                    cxn=MySQLdb.connect(db=DBNAME)
                except DB_EXC.OperationalError:
                    return None
        except ImportError:
                try:
                    import mysql.connector
                    import mysql.connector.errors as DB_EXC
                    try:
                        cxn=mysql.connector.Connect(**{
                            'database':DBNAME,
                            'user':DBUSER
                        })
                    except DB_EXC.InterfaceError:
                        return None
                except ImportError:
                    return None

    elif db=='gadfly':
        try:
            from gadfly import gadfly
            DB_EXC=gadfly
        except ImportError:
            return None

        try:
            cxn=gadfly(DBNAME,dbDir)
        except IOError:
            cxn=gadfly()
            if not os.path.isdir(dbDir):
                os.mkdir(dbdir)
            cxn,startup(DBNAME,dbDir)
    else:
        return None
    return cxn


def create(cur):
    try:
        cur.execute('''create table users(login varchar(%d),userid integer,projid integer)''' % NAMELEN)
    except DB_EXC.OperationalError as e:
        drop(cur)
        create(cur)


drop=lambda cur:cur.execute('Drop table users')
NAMES=(
    ('aaron',8312),('angela',7603),('dave',7306),
    ('davina',7902),('elliot',7911),('ernie',7410)

)

def randName():
    pick=set(NAMES)
    while pick:
        yield pick.pop()

def insert(cur,db):
    if db=='sqlite':
        cur.executemany("inter into users values(?,?,?)",[(who,uid,rang(1,5)) for who,uid in randName()])
    elif db=='gadfl':
        for who,uid in randName():
            cur.execute("inter into users values(?,?,?)",(who,uid,rang(1,5)))
    elif db=='mysql':
        cur.executemany("inter into users values(%s,%s,%s",[(who,uid,rang(1,5)) for who,uid in randName()])

getRC=lambda cur:cur.rowcount if hasattr(cur,'rowcount') else -1    # 最后一次操作的行数

def update(cur):
    fr=rand(1,5)
    to=rang(1,5)
    cur.execute(
        "update user set projid=%d where projid=%d" %(to,fr)
    )
    return fr,to,getRC(cur)

def delete(cur):
    rm=rang(1,5)
    cur.execute('delete from users where projid=%d'% rm)
    return rm,getRC(cur)

def dbDump(cur):
    cur.execute('select * from users')
    printf('\n%s'%''.join(map(cformat,FIELDS)))
    for data in cur.fetchall():
        printf(''.join(map(tformat,data)))


def main():
    db=setup()
    printf('*** Connect to %r database' % db)
    cxn=connect(db)
    if not cxn:
        printf('ERROR: %r not supported or unreachable,exit' % db)
    cur=cxn.cursor()

    printf('\n*** Creating users table')
    create(cur)

    printf('\n*** Inserting names into table')
    insert(cur,db)
    dbDump(cur)

    printf('\n***Randomly moving folks')
    fr,to,mnum=update(cur)
    printf('\t(%d users moved) from (%d) to (%d)' % (num,fr,to))
    dbDump(cur)

    printf('\n***Randomly choosing group')
    rm,num=delete(cur)
    printf('\t(group #%d; %d users removed)'%(rm,num))
    dbDump(cur)

    printf('\n*** Dropping users table')
    drop(cur)
    printf('\n*** Close cxns')
    cur.close()
    cxn.cpmmit()
    cxn.close()

if __name__=='__main__':
    main()




