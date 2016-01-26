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

p = P()
c = C()
d = D()

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


t1 = Time101(1, 23)
t2 = Time101(12, 54)
print t1, t2
print "*" * 88
print id(t1), id(t2)
s = t1 + t2
print s, id(s)

t1 += t2
print t1, id(t1)
# print t2 + 3
