#coding:utf8

__author__ = 'flybird1971'

#对象练习

import time,abc

class InterfaceDemo(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def eat(self):
        pass

    def sleep(self,times):
        print "start sleep ... "
        time.sleep(times)
        print "wark ... "
        pass

class Demo(InterfaceDemo):

    #静态属性
    desc = 'this is demo class '

    #构造方法
    def __init__(self,name,ruming):
        self.name = name  #动态公益属性
        self.__ruming = ruming #动态私有属性

    def eat(self):
        print "eating.."

    #public 方法
    def show(self):
        print self.desc

    #魔术方法
    def __call__(self, *args, **kwargs):
        print "call"

    #私有方法
    def __privateMethon(self):
        print "this is private methon ... "

    #静态方法
    @staticmethod
    def staticMethon():
        print "this is static methon ..."
    #属性方法
    @property
    def getProperty(self):
        return self.__ruming

    #析构
    def __del__(self):
        print u"析构"



demo = Demo('aa',u'乳名')
demo()
print demo.getProperty
#demo.__privateMethon
#demo.__ruming
demo.show()
demo.eat()
demo.sleep(3)