#!/usr/bin/env python
# coding:utf8


class Parent(object):
    """base class to test OOP
    for testing...
    """

    def __init__(self, name, age=12):
        self.name = name
        self.age = age
        self.__parent_doc = 'parent_doc'
        print "init parent class  .... "

    def updateName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def updateAge(self, age):
        self.age = age

    def getAge(self):
        print self.__parent_doc
        return self.age

    def __del__(self):
        print "delete parent class  .... "


class Chird(Parent):

    """son class to test inhreat
    for testing.....
    """

    def __init__(self, name, sex, age=12):
        Parent.__init__(self, name, age)
        self.__sex = sex
        print "init Chird class  .... "

    def getSex(self):
        return self.__sex

    def __del__(self):
        Parent.__del__(self)
        print "delete Chird class  .... "

# parent = Parent('father', 33)
son = Chird('son', 'male')

# print "*" * 88
# print "Class.__name__\t:\t", Chird.__name__
# print "\nClass.__doc__\t:\t", Chird.__doc__
# print "instance.__doc__\t:\t", son.__doc__
# print "Class.__base__\t:\t", Chird.__base__
# print "\nClass.__dict__\t:\t", Chird.__dict__
# print "\ninstance.__dict__\t:\t", son.__dict__
# print "\nClass.__module__\t:\t", Chird.__module__
# print "instance.__module__\t:\t", son.__module__
# print "\nClass.__class__\t:\t", Chird.__class__
# print "instance.__class__\t:\t", son.__class__
