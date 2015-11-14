#!/usr/bin/env python
#coding:utf8
import sys,os,re
import  admin_index
import  bank_index
import  shop_index
import bank.utils as utils
"""
    app入口
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""

service = [{u'银行测试入口':bank_index.index},
           {u"商城后台入口":admin_index.index},
           {u"商城入口":shop_index.index}]

def index():
    """
    app入口
    """
    while True:
        num = utils.printTableX(service)
        if num == -1:return False
        result = service[num].values().pop()()
        print u"\n\n************************* app主界面 *******************************\n"
    print u"------------- end -------------"
    return True



if __name__=='__main__':
    index()