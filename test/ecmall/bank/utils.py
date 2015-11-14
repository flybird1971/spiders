#!/usr/bin/env python
#coding:utf8
import hashlib,random,time

"""
工具函数
"""

def encrypt(str):
    """
    用于注册用户加密
    """
    hash = hashlib.md5()
    hash.update(str)
    return hash.hexdigest()

def uniqueNo():
    """
    生成银行卡号
    """
    cardNo = []
    for t in xrange(18):
        cardNo.append(str(random.randint(0,9)))
    return ''.join(cardNo)

def printTable(data):
    """
    打印表格
    """
    index = 0
    for tmp in data:
        numLine = len(tmp)
        strformat = ""
        while numLine>=0:
            strformat = strformat + "| \t\t\t %s \t\t\t "
            numLine = numLine - 1
        strformat = strformat
        print "-"*66
        print strformat % (index,tmp.keys().pop())
        index = index + 1
    return True