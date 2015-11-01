#!/usr/lib/env python
#coding:utf8
"""
author : flybird1971@gmail.com
since  : 2015-11-01 13:43:23
"""

def show(name,age,sex='man',*argsList,**argsDic):
    print """
            name : %s
            age   : %s
            sex   : %s"""  % (name,age,sex)
    print argsList,argsDic
    return True

show("lixue",23)
show('zs',sex='women',age='223')

#122 会作为key被 **argDic接受，无对应value，会报错
#show('zs',sex='women',age='223',122)

show('db','aa',12,122)
show('db','aa','ddd','222','eeee',ohter='dddd',ass='eeee')

print "*"*22
arglist = ['liu',12,'women','aaa','eeee']
show(*arglist)

argtuple = ('lius',22,'man','eee',23)
show(*argtuple)

argdic = {'name':'liu','age':12,'sex':'man','other':'eee'}
show(**argdic)
#333会作为 key被**argsDic接受，但无对应value 会报错
#show('db','aa','ddd','222',ohter='dddd',333)
""""
默认  实参依次赋值给 形参
当 key = value形式存在时，
   如果有对应形参key，value会赋值给对应形参，
   如果没有对应形参key,会被**argsDic接收，并且后面的都必须是 key=>value形式，因为*argsList 只接收多于的value,碰到
   key=>value ,以后所有多于参数都会被**argsDic处理
"""

print "*"*88
def myXreadlines(path):
    """
     param path: 文件路径
    return: 文件每行数据
    """
    pos = 0
    while True:
        with open(path,'rb') as f:
            f.seek(pos)
            data = f.readline()
            if not data : return
            yield  data
            pos = f.tell()

for line in myXreadlines('../data/ts.json'):
    print line



"""
   内置函数

"""
print "-"*88
#help()
print dir()
print vars()
print type(list)
#reload()

class myGenerator():
    def __init__(self,callback):
        callback()

    def next(self):
        print 'data'



