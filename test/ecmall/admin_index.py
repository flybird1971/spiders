#!/usr/bin/env python
#coding:utf8
from shopAdmin import config
from shopAdmin import login
from shopAdmin import good
import sys,os,re
sys.path.insert(1,os.path.realpath('..'))
import bank.utils as utils
"""
    商城后台入口
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""

service = [{u'登录':login.show},
           {u"配置":config.show},
           {u"操作商品":good.show}]

def index():
    """
    商城后台相关操作入口
    """
    while True:
        num = utils.printTableX(service)
        if num == -1:return False
        result = service[num].values().pop()()
        print u"\n\n************************* 商城后台主界面 *******************************\n"
    print u"------------- end -------------"
    return True



if __name__=='__main__':
    index()