#!/usr/bin/env python
#encoding:utf8
from __future__ import division
from random import randint
__author__ = 'flybird1971'

def cule(money):
    if(money>1) : return False
    money = int(money*100)
    fen25 = fen10 = fen5 = fen1 = 0

    shenyu = money;
    fen25,shenyu = divmod(money,25)
    fen10,shenyu = divmod(shenyu,10)
    fen5,fen1 = divmod(shenyu,5)

    return {'25':fen25,'10':fen10,'5':fen5,'1':fen1}


res = cule(0.98)
print res


def huashi2sheshi(sheshi):
    return (sheshi-32)*(5/9)

print huashi2sheshi(120)


def yearIncome(rate):
    i = 0
    tmp = 1
    while i<365:
        tmp = tmp * (1+rate)
        i+=1
    return tmp-1

print yearIncome(0.00009)



def randos(n):
    li = []
    for i in xrange(randint(2,100)):
        li.append(randint(0,2**31-1))

    print "total %s " % (len(li))
    print li

    res = []
    lenght = len(li) - 1
    for i in xrange(randint(1,100)):
        index = randint(0,lenght)
        res.append(li[index])
    print "after total %s " % (len(res))
    print res
    res.sort()

    return res

print "="*88
print randos(100)

strObj = basestring('a')


























