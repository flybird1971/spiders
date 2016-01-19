#!/usr/bin/env python
# coding:utf8

from random import randint

strTmp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'


def randStr(length=12):

    resStr = []
    length = length if length > 0 else 0
    strLen = len(strTmp) - 1
    while length > 0:
        resStr.append(strTmp[randint(0, strLen)])
        length -= 1
    return "".join(resStr)


def randInt(length=12, minVal=1, maxVal=9999):
    return [randint(minVal, maxVal) for i in xrange(length)]
