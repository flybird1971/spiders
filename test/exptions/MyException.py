#!/usr/bin/env python
# coding:utf8

__author__ = 'flybird1971'
class MyException(Exception):

    def __init__(self,msg):
        self.message = msg

    def __str__(self):
        return self.message



if __name__=='__main__':
    try:
        raise MyException("中国")
    except MyException,e:
        print e

