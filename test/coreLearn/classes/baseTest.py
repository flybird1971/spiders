#!/usr/bin/env python
# coding:utf8

class Father(object):

    total = 0

    def __init__(self,name,age=18):
        self.name = name
        self.__age = age

    def getName(self):return self.name

    def setAge(self,age):self.__age = age

f = Father('joke',12)
print dir(Father)
print "-"*180
print Father.__class__
print Father.__dict__
print "*"*180
print vars(Father)
print "*"*180
print dir(f)
print "-"*180
print f.__class__,f.__dict__
print "-"*180
print vars(f)



# print type(f)
# print type(Father)