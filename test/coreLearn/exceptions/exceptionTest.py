#!/usr/bin/env python
# coding:utf8
import __init__
from utils.CollectionHelper import CollectionHelper

try:
    # raise ArithmeticError,'nnnn'
    f = open('xxx.xxx', 'r')
except (Exception, NameError, ZeroDivisionError, IOError, SyntaxError,
        IndexError, KeyboardInterrupt, KeyError, ArithmeticError), e:
    print "has error %s " % str(e)
else:
    pass
finally:
    pass

print "*" * 88
try:
    raise TypeError, 'type error'
    raise ValueError, 'value error'
    pass
except Exception, e:
    print "has error %s " % str(e)
except ValueError, e:
    print "has error %s " % str(e)
except TypeError, e:
    print "has error %s " % str(e)
else:
    print "no error s "
finally:
    print "finally "
    pass


def set_float(amount):
    try:
        amount = float(amount)
    except (ValueError, TypeError), e:
        amount = str(e)
    return amount

print "-" * 88


def checkAmount():
    fLog = open('../../data/amount.json.demo', 'a+')
    try:
        fAccount = open('../../data/amount.data', 'r')
    except IOError, e:
        fLog.write("no txns this month\n")
        fLog.close()
        return None

    fLog.write("-------------------begin--------------------\n")
    dataArr = fAccount.readlines()
    fAccount.close()

    totalAccount = 0
    for line in dataArr:
        tmpAccount = set_float(line)
        if isinstance(tmpAccount, float):
            totalAccount += tmpAccount
            fLog.write("add acount  %s \n" % tmpAccount)
        else:
            fLog.write("ingore %s \n" % tmpAccount)
    fLog.close()
    print "total money is : %.2f " % tmpAccount
    return None
checkAmount()

try:
    raise TypeError, ('has error ', 12)
    with open('../../data/amount.json.demos1', 'r') as f:
        CollectionHelper.printEx(f.readlines())
except (IOError, TypeError), e:
    print "has error %s " % str(e)

print "*" * 88
assert 1 == 2
