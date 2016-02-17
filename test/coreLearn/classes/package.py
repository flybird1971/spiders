#!/usr/bin/env python
# coding:utf8

class Wrapping(object):
    
    def __init__(self,data):
        self.__data = data

    def __repr__(self):
        return "this is packegaed class : %r " % self.__data

    def __str__(self):
        return str(self.__data)

    def get(self):
        return self.__data

    def __getattr__(self,attr):
        return getattr(self.__data,attr)


w = Wrapping(['test','man',123,True,{'ok':'te'}])

print w
w.append('last insert')
print w
print w.index('man')
print w.count(123)
print w.pop()