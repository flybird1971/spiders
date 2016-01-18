#!/usr/bin/env python
# ecoding:utf8
from __future__ import division

def testBoolean():
    print True
    print True + 2 
    print 2.5 + 6j
    x = True
    print x

def tranVal(x,y):
    print x,y
    x,y = y,x
    print x,y

def test_one():
    x = 12
    y = 21
    print x,y

    print "*"*77
    x = y = 23
    print x,y
    y = 32
    print x,y
    print "*"*88
    z = 43
    x = y = z
    print x,y,z

    z = 54
    print x,y,z

f = open(r'..\\data\\test_one.json','a+')
f.write('hello,world')
f.close()

print 0<1 and 10>9 or 0>1
print (3 is 4 ) != 0

print "*"*45
x = 0
while x < 10:
    x += 1
    if x==9:
        continue
    print "h",
else:
    print "good"

print "*"*88
