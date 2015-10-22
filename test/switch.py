#encoding:utf8
from __future__ import division

__author__ = 'flybird1971'

#中午
print(5/2)
print("*"*32)

def jia(x,y):
    return x+y

def jian(x,y):
    return x-y

def cheng(x,y):
    return x*y

def chu(x,y):
    return x/y

operators = {'+':jia,'-':jian,'*':cheng,'/':chu}

print operators['+'](2,3)
print operators['-'](2,3)
print operators['*'](2,3)
print operators['/'](2,3)


print operators.get('*')(3,4)