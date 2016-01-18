#!/usr/bin/env python
# encoding:utf8
import os
import sys
import string
sys.path.insert(1, os.path.realpath('../../'))
from utils.CollectionHelper import CollectionHelper
from exptions.MyException import MyException


# print help(string)
# CollectionHelper.printEx(dir(string))

li1 = range(12, 35, 3)
li2 = range(4, 67, 6)
# print li1 + li2
# print li1.extend(li2)

# print li1[::-1]  # 序列的反转
li = dir(list)
# print "-"*88
# print li
print "-"*88
strObj = 'abcefghijklmnopq'
# print tuple(strObj)
# print list(strObj)
# CollectionHelper.printEx(dir(list))

class Idcheck(object):

    keywords = ['class','int','float','str','string','list',
                'tuple','dict','add','remove','len']

    reverseWords = []

    @staticmethod
    def check(words):
        """[summary]
        Arguments: words 
        Returns: bool 
        Raises:  MyException -- [description]
        """
        if len(words)<1 :
            raise MyException, "word must length 0 char"

        if words in Idcheck.keywords + Idcheck.reverseWords:
            raise MyException ,"%s is keywords or reverse words" % (words)

        if words[0] not in string.letters+"_" :
            raise MyException , "first char must is _ or "+','.join(list(string.letters))

        if len(words) == 1:
            return True

        checkStr = words[1:]
        collectStr = string.letters + "_" + string.digits
        for tmpChar in checkStr:
            if tmpChar not in collectStr:
                raise MyException , " must is "+','.join(list(collectStr))
        else:
            return True


if __name__ =="__main__":

    while True:
        inputStr = raw_input("plase enter one word or enter 'q' to exits ")
        if inputStr == 'q': break;
        try:
            Idcheck.check(inputStr)
            print inputStr,"is ok "
        except MyException,e :
            print e

    else:
        print "you stop test"
