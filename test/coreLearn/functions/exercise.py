#!/usr/bin/env python
# coding:utf8
import os
import sys
import string
import re
from random import randint
import __init__
from utils.randString import randStr, randInt

"""本模块主要是 11章课后练习
"""

# 11-3 题解


def max2(one, two):
    return one if one > two else two


def min2(one, two):
    return one if one < two else two


def maxEx(sequence, maxFun=max2):
    if not len(sequence):
        return None

    maxEle = sequence[0]
    for ele in sequence:
        maxEle = maxFun(maxEle, ele)
    return maxEle


def minEx(sequence, minFun=min2):
    if not len(sequence):
        return None

    minEle = sequence[0]
    for ele in sequence:
        minEle = minFun(minEle, ele)
    return minEle


print max2(2, 32)
print max2(3, 3)
print max2('a', 3)
print max2('c', 'z')
print max2('a', 'a')

print "*" * 88
print min2(2, 32)
print min2(3, 3)
print min2('a', 3)
print min2('c', 'z')
print max2('a', 'a')


testDict = randInt()
testTuple = tuple(testDict)
testStr = randStr(32)

print testDict
print maxEx(testDict), minEx(testDict), sorted(testDict)
print ""
print testTuple
print maxEx(testTuple), minEx(testTuple), sorted(testTuple)
print ""
print testStr
print maxEx(testStr), minEx(testStr), sorted(testStr)

# 11-4

print "*" * 88


def toMinutes(hour, minutes):
    resMinutes = 0
    resMinutes += int(hour) * 60 + int(minutes)
    return resMinutes


def formatTime(minutes):
    minutes = int(minutes)
    hour = minutes // 60
    minutes = minutes % 60
    return hour, minutes

print toMinutes(1, 23)
print formatTime(toMinutes(3, 21))


# 11-5

def countMoney(price, tax=0.17):
    return int(price) * (tax + 1)

print countMoney(12)
print countMoney(31, 0.2)

# 11-6
formatSymbol = {'%d': int, '%s': str, '%f': float}


def findFormatSymbol(formatStr):

    if not formatStr:
        return None

    regex = r'(' + "|".join(formatSymbol.keys()) + ')'
    pattern = re.compile(regex, re.I | re.M)
    return pattern.findall(formatStr)


def formatString(formatStr, requiredFormat, *mapVal):

    if len(requiredFormat) > len(mapVal):
        raise Exception, 'requiredFormat less mapVal'

    for i in range(len(requiredFormat)):
        try:
            tmpVal = formatSymbol[requiredFormat[i]](mapVal[i])
            formatStr = re.sub(r'' + requiredFormat[i] + '', str(tmpVal), formatStr, 1, re.I | re.M)
        except Exception, e:
            raise Exception, "%s can not converse %s " % (mapVal[i], str(formatSymbol[requiredFormat[i]]))
    return formatStr


def printf(formatStr, *mapVal):
    requiredFormat = findFormatSymbol(formatStr)
    formatedStr = formatString(formatStr, requiredFormat, *mapVal)
    print formatedStr

printf('test %d test %f test %wdr test %s test %d test %f test %r ', '12', '2.1', '12abc', '33', '3.55')


# 11-7

print "*" * 88


def myZip(*sequenceTuple):
    return map(None, *sequenceTuple)

print myZip(range(11), [randStr(randint(0, i)) for i in xrange(12)])

print zip(range(11), [randStr(randint(0, i)) for i in xrange(12)])


# 11-8

print "*" * 88


def getBissextile(year):
    """判断是否是闰年
    """
    if (not year % 4):
        if (not year % 400) or year % 100:
            return True
    return False

print filter(getBissextile, range(1900, 2016 + 1))

# 11-9

print "*" * 88


def average(sequence):
    total = reduce((lambda x, y: x + y), sequence, 0)
    return float(total) / len(sequence)

print average(range(3, 100, 7))
