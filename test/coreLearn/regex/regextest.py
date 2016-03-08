#!/usr/bin/env python
#coding:utf8

import re

# match
m = re.match('foo','sfood is good',re.M)
print m

if m:
    print m.group()
    print m.groups()

m2 = re.match('f(\w)(\d)','fo1 tst fo2 es fe3')
print m2
if m2:
    print m2.group(2)
    print m2.groups()


# search
print "*"*88
s = re.search('foo','sfood is sfood is good')
print s
if s:
    print s.group()
    print s.groups()

s2 = re.search('f(\w)*(\d)*','sfo1d is sfo2 test sfwset43 nma sfced523 ')
if s2:
    print s2.group()
    print s2.groups()


# .
print "*"*88
dot = re.search('.name','\r\tname')
print dot
if dot:
    print dot.group()


allregex = re.findall(r'(a((\w+)c))','abc,eft,cde,acc,ew,aec,wee,aqc')
if allregex:
    print allregex

t = type(dir)
typeRegex = re.compile(r'<type\s+\'(\w+?)\'>')
res = typeRegex.search(str(t))
print res
if res :
    print res.group(1)