#!/usr/bin/env python
# encoding:utf8
# import module

from module.module import randStr
import string
# 导入包
import pack.testPack as test
__author__ = 'flybird1971'

timer = 1
while True:
    if timer > 10:
        break
    timer += 1
    print string.capitalize(randStr(timer))

print "*"*32
test.show()

