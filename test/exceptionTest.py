#coding:utf8

__author__ = 'flybird1971'

try:
    f = open("aaaa")
except IOError,e:
    print "error infos : %s " % (e.errno )
except NameError,e:
    print "variable not defined"


print "haha"