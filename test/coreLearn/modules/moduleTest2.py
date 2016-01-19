#!/usr/bin/env python
# coding:utf8

import __init__
from utils.CollectionHelper import CollectionHelper

"""[summary]

[description]
"""
name = 'joke'
age = 12
tips = 'show tips the flowing ... '
__esc = 'sssss'


def test(name):
    info = 'hello world'

    def sonTest(do):
        name = 'son demo'
        print "this is son function; name : %s " % name
        print "local son function globals and locals "
        CollectionHelper.printEx(globals())
        print "*" * 22 + "local" + "*" * 22
        CollectionHelper.printEx(locals())

    sonTest(info)
    print "-------------- local test function globals and locals -------------- "
    CollectionHelper.printEx(globals())
    print "*" * 22 + "local" + "*" * 22
    CollectionHelper.printEx(locals())
    return None

test(name)
print "-------------- top globals and locals -------------- "
CollectionHelper.printEx(globals())
print "*" * 22 + "local" + "*" * 22
CollectionHelper.printEx(locals())
