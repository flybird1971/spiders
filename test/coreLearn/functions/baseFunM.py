#!/usr/bin/env python
# coding:utf8

from operator import add,sub
from random import randint,choice

ops = {'+':add,'-':sub}
MAX_RUN_TIMES = 2

def doprob():
    """随机运算加法或减法
    """ 
    times = 0
    randOperator = choice('+-')
    nums = [randint(1,10) for i in range(2)]
    nums.sort(reverse=True)
    tips = " %s %s %s = " % (nums[0],randOperator,nums[1])
    ans = ops[randOperator](*nums)

    while True:
        try:
            inp = raw_input(tips)
            if int(inp) == ans:
                print "it is right!"
                break
            elif times == MAX_RUN_TIMES:
                print """you has no times to play !!
                asn : %s %s
                """ % (tips,ans)
                break
            else :
                print " you are wrong ! try againt "
                times += 1
        except Exception, (KeyboardInterrupt,EOFError,ValueError):
            break
        

def main():
    while True:
        doprob()
        try:
            isGo = raw_input('try againt ,yes or no : ')
            if isGo and isGo[0].lower()=='n':
                print "Good By!!!"
                break
        except Exception, (KeyboardInterrupt,EOFError):
            break
            print "has inner error "


main()