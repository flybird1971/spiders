#!/usr/bin/env python
#coding:utf8
__author__ = 'flybird1971'

def outer (fun):
    def wrapper():
        print "\n\n++++++++++++++++++++++++++++++++"
        print "before action"
        fun()
        print "after action"
    return wrapper

@outer
def fun_1():
    print "login..."

@outer
def fun_2():
    print "logout...."

@outer
def fun_3():
    print "view...."

fun_1()
fun_2()
fun_3()