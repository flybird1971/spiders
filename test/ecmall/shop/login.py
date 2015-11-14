#!/usr/bin/env python
#coding:utf8
import  sqlOperator as sql
import sys,os
sys.path.insert(1,os.path.realpath('..'))
import bank.utils as utils
"""
    用户登录商城验证
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""
def login(user,passwd):
    userInfo = sql.getUser(user)
    if not userInfo:
        print u"用户或者密码错误"
        return  False
    passwd = utils.encrypt(passwd)
    if user==userInfo.get('user') and passwd==userInfo.get('password'):
        return True
    print u"用户或者密码错误"
    return  False

def loginStart():
    user = raw_input(u"请输入用户名：")
    passwd = raw_input(u"请输入密码：")
    if not login(user,passwd):
        return False
    sql.markLoginSuccess(user)
    print u"登录成功"
    return True

def show():
    print u"\n\n\n +++++++++++++你已经进入商城后台登录中心 ：  +++++++++++++"
    loginStart()

if __name__=='__main__':
    show()