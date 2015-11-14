#!/usr/bin/env python
#coding:utf8
import hashlib,random,time,re

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

def printTableX(data):
    """
    打印表格
    """
    index = 0
    for tmp in data:
        numLine = len(tmp)
        strformat = ""
        while numLine>=0:
            strformat = strformat + "|\t\t\t%s\t\t\t"
            numLine = numLine - 1
        strformat = strformat
        print "-"*66
        print strformat % (index,tmp.keys().pop())
        index = index + 1

    while True:
        num =  raw_input(u"请选择对应服务 或者 输入q退出 ：")
        if num == 'q': return -1
        regex = re.compile(r"\d+")
        if (not regex.match(num))  or (  int(num) >= len(data)):
            print u"请输入正确服务号码"
            continue
        num = int(num)
        break
    return num

def printGoods(data):
    """
    打印商品列表
    """
    if not data :
        print u"无商品"
        return  False

    fields = ['id',u'商品名称',u'商品类型',u"商品价格",u"商品数量"]
    numLine = len(fields)
    strformat = ""
    while numLine>0:
            strformat = strformat + "|\t\t%-12s\t\t"
            numLine = numLine - 1
    print "-"*150
    print strformat % tuple(fields)

    for tmp in data:
        numLine = len(tmp)
        strformat = ""
        while numLine>0:
            strformat = strformat + "|\t\t%-12s\t\t"
            numLine = numLine - 1
        print "-"*150
        print strformat % (tmp.get('id'),tmp.get('name'),tmp.get('type'),tmp.get('price'),tmp.get('num'))
    return True
