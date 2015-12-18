# coding:utf8

import time
import abc
__author__ = 'flybird1971'

# 对象练习


class InterfaceDemo(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def eat(self):
        pass

    def sleep(self, times):
        print "start sleep ... "
        time.sleep(times)
        print "wark ... "
        pass


class Demo(InterfaceDemo):

    # 静态属性
    desc = 'this is demo class '

    # 构造方法
    def __init__(self, name, ruming):
        self.name = name  # 动态公益属性
        self.__ruming = ruming  # 动态私有属性

    def eat(self):
        print "eating.."

    # public 方法
    def show(self):
        print self.desc

    # 魔术方法
    def __call__(self, *args, **kwargs):
        print "call"

    # 私有方法
    def __privateMethon(self):
        print "this is private methon ... "

    # 静态方法
    @staticmethod
    def staticMethon():
        print "this is static methon ..."
    # 属性方法

    @property
    def getProperty(self):
        return self.__ruming

    # 析构
    def __del__(self):
        print u"析构"


demo = Demo('aa', u'乳名')
demo()
print demo.getProperty
# demo.__privateMethon
# demo.__ruming
demo.show()
demo.eat()
demo.sleep(3)


class SubOne(Demo):
    pass


class SubTwo(Demo):
    pass


print Demo.desc, SubOne.desc, SubTwo.desc

SubOne.desc = 'this is son one demo '
print Demo.desc, SubOne.desc, SubTwo.desc

Demo.desc = ' modifty base class demoe description '
print Demo.desc, SubOne.desc, SubTwo.desc

SubTwo.desc = ' modifty son two description'
print Demo.desc, SubOne.desc, SubTwo.desc

print "*" * 80
li = [lambda x: x**x for x in range(5)]
print li

while True:
    inputStr = raw_input("请输入数字或'q'退出：")
    if inputStr == 'q':
        break
    print "你输入字符串：%s " % (inputStr)

demo = Demo()
demo.show()
