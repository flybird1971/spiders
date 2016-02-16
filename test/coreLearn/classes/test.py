#!/usr/bin/env python
# coding:utf8

# from baseTest import Chird

# m = Chird('joke', 'mele')
# print type(m)


class Demo(object):
    version = 1.1

    def show(self):
        print Demo.version

    @staticmethod
    def showEx(tags):
        print tags

# d = Demo()
# d.showEx('instance')
# Demo.showEx('demo')


# d = Demo()
# d.show()
# Demo.show(d)

# print "*" * 88
# print d.version
# print Demo.version
# print "*" * 88
# d.version += 12
# print d.version
# print Demo.version


class P(object):
    pass


class C(P):
    pass


class D(object):
    pass

# p = P()
# c = C()
# d = D()

# print issubclass(C, P)
# print issubclass(P, P)
# print issubclass(D, P)
# print issubclass(P, (P, C, D))
# print "*" * 88
# print isinstance(d, D)
# print isinstance(d, C)
# print "*" * 88
# print isinstance(c, P)
# print isinstance(c, C)
# print isinstance(c, (C, P, D))
# print isinstance(1, int)


# print hasattr(p, 'show')
# def show(self, name):
#     print name
# setattr(p, 'show', show)
# p.show(p, 'eee')
# print getattr(p, 'show')
# print vars(p)
# print delattr(p, 'show')
# print vars(p)


class Time101(object):
    """
    time101 show time trace
    """

    def __init__(self, hr, mins):
        self.hr = hr
        self.mins = mins

    def __add__(self, obj):
        self.__class__.__checkType(obj, self.__class__)
        hr = self.hr + obj.hr
        mins = self.mins + obj.mins
        hr += (mins // 60)
        mins = mins % 60
        return self.__class__(hr, mins)

    def __iadd__(self, obj):
        self.__class__.__checkType(obj, self.__class__)
        self.hr = self.hr + obj.hr
        mins = self.mins + obj.mins
        self.hr += (mins // 60)
        self.mins = mins % 60
        return self

    def __str__(self):
        return "%s:%s" % (self.hr, self.mins)

    __repr__ = __str__

    @staticmethod
    def __checkType(obj, cls):
        assert isinstance(obj, cls), "type error "
        return True


# t1 = Time101(1, 23)
# t2 = Time101(12, 54)
# print t1, t2
# print "*" * 88
# print id(t1), id(t2)
# s = t1 + t2
# print s, id(s)

# t1 += t2
# print t1, id(t1)
# print t2 + 3


strd = """GET /?a=11&aa=22&ft=23 HTTP/1.1
Host: localhost:8080
Connection: keep-alive
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36
DNT: 1
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8


"""
import re


class ParseHeader(object):

    """解析header
    """

    def __init__(self, headerStr):
        self.headerStr = headerStr
        self.headerDict = {}

    def parse(self):
        if not self.headerStr:
            raise ValueError, 'header is empty'

        strd = self.headerStr.strip()
        regex = re.compile('[\r\n]+', re.M)
        headerInfos = regex.split(strd)
        regexTwo = re.compile(':\s+')

        # 特殊处理请求方式
        methodInfo = headerInfos[0].split(' ')
        self.headerDict[methodInfo[0]] = methodInfo[1]
        del headerInfos[0]

        self.headerDict.update(ParseHeader.__list2Dict(headerInfos, regexTwo))
        return self.headerDict

    def getGet(self):
        if not self.headerDict.get('GET', None):
            raise ValueError, 'get not is exits'

        getInfo = self.headerDict['GET']
        getInfo = getInfo.strip('/?')
        getInfoList = getInfo.split('&')

        regex = re.compile('=')
        getInfoDict = ParseHeader.__list2Dict(getInfoList, regex)
        return getInfoDict

    @staticmethod
    def __list2Dict(li, regex):

        if not li:
            raise ValueError, 'not is list type'

        result = {}
        for info in li:
            key, val = regex.split(info)
            result[key] = val
        return result

# phead = ParseHeader(strd)

# print phead.parse()
# print phead.headerDict.get('Host')
# print phead.getGet()
