#!/usr/bin/env python
#coding:utf8
from shop import car
from shop import login
from shop import pay
from shop import register
from shop import resetpwd
from shop import shoping
import sys,os,re
sys.path.insert(1,os.path.realpath('..'))
import bank.utils as utils
"""
    商城入口
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""

service = [{u'登录':login.show},
           {u"注册":register.apply},
           {u"重置密码":resetpwd.resetPwd},
           {u"购物":shoping.show},
           {u"查看购物车":car.show},
           {u"支付":pay.pay}]

def index():
    """
    商城购物操作入口
    """
    while True:
        num = utils.printTableX(service)
        if num == -1:return False
        result = service[num].values().pop()()
        print u"\n\n************************* 商城购物主界面 *******************************\n"
    print u"------------- end -------------"
    return True



if __name__=='__main__':
    index()