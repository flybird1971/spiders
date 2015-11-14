#!/usr/bin/env python
#coding:utf8
import sqlOperator as sql
import login
import register
import sys,os
sys.path.insert(1,os.path.realpath('..'))
import bank.utils as utils
from MyException.MyException import MyException
"""
    商城用户重置密码处理
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""

def resetPwd():
    """
    重置密码
    """
    print u"\n\n\n +++++++++++++你已经进入商城重置密码中心 ：+++++++++++++ "
    if not login.loginStart():
        print (u"登录失败，不能重置密码")
        return False

    try:
        print (u"---------------重置密码-----------------")
        passwd = register.inputPwd() #输入新密码
        passwd = utils.encrypt(passwd)
        user = sql.readLoginUser()
        sql.updateUser(user,{'password':passwd}) #更新数据
    except MyException,e:
        print e
        return False
    print u"密码重置成功"
    return True


if __name__ == "__main__":
    resetPwd()