#!/usr/bin/env python
# coding:utf8

from time import ctime, sleep, time
from random import randint
from operator import add, mul
from urllib import urlretrieve
from functools import partial
import Tkinter

"""function

关键字参数(字典)&非关键字参数(元组)
默认参数
参数组

demo functionName(postional_args,keywords_args,*tuple_args,**dict_args)
[description]
"""
# 参数类型（关键字参数，非关键字参数测试）


def showTest(host, port=80, isLong=False):
    isLong = 'yes' if isLong else 'no'
    print " %s:%s ,is long %s !!" % (host, port, isLong)

# showTest('127.0.0.1')
# showTest('127.0.0.1', isLong=True)

# 函数属性


def foo():
    "show foo function create"
    pass


def bar():
    pass

bar.__doc__ = "bar function create"
bar.version = '1.0'
# print help(foo)
# print help(bar)
# print bar.version
# print bar.__doc__

# 装饰器


def init(name):
    print "before action ..... "
    print " name is %s " % (name)
    print "after action .... "
    return init


@init('joke')
def prints():
    print "prints : %s " % ('s')


# prints('ok')


def trace(fun):
    print "装饰器begin....."

    def count(begin, end):
        print " %s %s " % (ctime(), fun.__name__)
        return fun(begin, end)
    print "装饰器end....."
    return count


@trace
def sm(begin, end):
    sum = 0
    for i in xrange(begin, end + 1):
        sum += i
    print "begin %s end %s sm is %s " % (begin, end, sum)


# for i in xrange(5):
#     nums = [randint(1,100) for i in xrange(2)]
#     nums.sort()
#     sm(*nums)
#     sleep(3)


print "*" * 88

# 有参装饰器


def decoratorWithArgs(name, doc):
    print "有参装饰器beign......"

    def demo(fun):
        def work(begin, end, defaultArg=name, defaultArg2=doc):
            sum = 0
            for i in xrange(begin, end + 1):
                sum += i
            print "begin %s end %s sm is %s " % (begin, end, sum)
            fun(begin, end)
        return work

    print "有参装饰器end......"
    return demo


@decoratorWithArgs('joke', 'decorator with args !!!!')
def sumX(begin, end):
    print "it is ok"

print type(sumX)
# sumX(1,3)


print "*" * 88

# 函数别名 & 作为参数传递 & 引用 & 调用


def conv(fun, sequence):
    return [fun(i) for i in sequence]

# testData = (2,2.1,-23)
# print conv(int,testData)
# print conv(long,testData)
# print conv(float,testData)


print "*" * 88


def getFirstLine(lines):
    for line in lines:
        if not line.strip():
            continue
        return line
    return ''


def firstLast(contents):
    try:
        f = open(contents)
        lines = f.readlines()
        f.close()
        first = getFirstLine(lines)
        lines.reverse()
        last = getFirstLine(lines)
        return first, last
    except Exception, IOError:
        f.close()


def download(url, proccess=firstLast):
    try:
        result = []
        retval = urlretrieve(url)[0]
        if retval:
            result = proccess(retval)
        return result
    except Exception, IOError:
        print "has error"

url = "http://blog.csdn.net/lanyuanershe/article/details/8083425"
url = "http://www"
# print download(url)

print "*" * 88
# 变长参数列表 【无关键字变长参数列表，关键字变长参数列表】


def testUnit(fun, *tupleArgs, **dictArgs):
    try:
        tmpRes = fun(*tupleArgs, **dictArgs)
        result = fun.__name__ + str(tupleArgs) + str(dictArgs) + " : " + str(tmpRes)
    except Exception, e:
        result = "fail " + str(e)
    finally:
        return result

dictMap = (int, long, float)
valueArr = [1, 2.1, -45]

# for funs in dictMap:
#     for val in valueArr:
#         print testUnit(funs, val)

print "*" * 88

# 匿名函数 lambda
# t = lambda *args: [i for i in args]
# print t()
# print t(1, 2, 3, 4, 5, 6)
# t = lambda x=23: x**x
# print t()
# print t(2)
testData = range(1, 30)
# print reduce((lambda x, y: x + y), testData)
# print map((lambda x: x**x), testData)
# print map(None, testData, testData, testData)
# print zip(testData, testData, testData)
# print filter((lambda x: x % 2), testData)


print "*" * 88
# 偏函数
add100 = partial(add, 100)
# print add100(4)

# root = Tkinter.Tk()
# MyButton = partial(Tkinter.Button, root, fg='white', bg='blue')
# b1 = MyButton(text='Button_one')
# b2 = MyButton(text='Button_two')
# qb = MyButton(text='quit', bg='red', command=root.quit)

# b1.pack()
# b2.pack()
# qb.pack(fill=Tkinter.X, expand=True)
# root.title('PFAs')
# root.mainloop()
bin2hex = hex(int('101010', 2))
# print bin2hex


print "*" * 88

# 闭包
output = "<int %r id=%#0x val=%d>"
w = x = y = z = 1


def f1():
    x = y = z = 2

    def f2():
        y = z = 3

        def f3():
            z = 4
            print output % ('w', id(w), w)
            print output % ('x', id(x), x)
            print output % ('y', id(y), y)
            print output % ('z', id(z), z)

        clo = f3.func_closure
        if clo:
            print "f3 closure vars : ", [str(c) for c in clo]
        else:
            print "no f3 closure vars"
        f3()

    clo = f2.func_closure
    if clo:
        print "f2 closure vars : ", [str(c) for c in clo]
    else:
        print "no f2 closure vars"
    f2()

clo = f1.func_closure
if clo:
    print "f1 closure vars : ", [str(c) for c in clo]
else:
    print "no f1 closure vars"
f1()


print "*" * 88

# 闭包 & 装饰器


def loggend(when):

    def log(f, *nkargs, **kargs):
        print """Call Back
        function %s
        no_keywords_args %r
        keywords_args %r
        """ % (f, nkargs, kargs)

    def preLog(f):
        def wrapper(*nkargs, **kargs):
            log(f, nkargs, kargs)
            return f(*nkargs, **kargs)
        return wrapper

    def postLog(f):
        def wrapper(*nkargs, **kargs):
            now = time()
            try:
                return f(*nkargs, **kargs)
            finally:
                log(f, nkargs, kargs)
                print " cost time %s " % (time() - now)
        return wrapper

    try:
        return {'pre': preLog, 'post': postLog}[when]
    except (Exception, TypeError), e:
        print "has error %s " % (str(e))


@loggend('pres')
def show(name):
    print "name is %s " % (name)

show('joke')
