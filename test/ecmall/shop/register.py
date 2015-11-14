#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re,sys,os
sys.path.insert(1,os.path.realpath('..'))
import bank.utils as utils
from MyException.MyException import MyException
import sqlOperator as sql
"""
    注册商城用户
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""

def inputUser():
    """
    读入用户名
    """
    user = None
    while True:
        user = raw_input(u"请输入用户名 或者 输入q退出 : ")
        if user == 'q':
            raise MyException,"logout....."
        regex = re.compile(r'^\w{6,15}$')
        if not regex.match(user):
            print u"warn : 你输入的用户名格式不正确，请重新输入 或者 输入q退出 ！"
            continue
        break
    return user

def inputPwd():
     """
    设置密码,并进行格式合法验证
    """
     passwd = None
     while True:
        passwdTmp = raw_input(u"请输入密码 或者 输入q退出 : ")
        if passwdTmp == 'q':
            raise MyException,"logout...."
        regex = re.compile(r'\w{6,15}')
        if not regex.match(passwdTmp):
            print u"warn : 密码6-15位，只能是字母数字下划线，请重新输入 或者 输入q退出 ！"
            continue
        passwd = passwdTmp
        break
     return passwd

def apply():
    """
    注册商城用户
    """
    print u"\n\n\n +++++++++++++你已经进入商城注册中心 ： +++++++++++++ "
    try:
        user   = inputUser() #读入用户名
        passwd = inputPwd() #输入密码
        passwd = utils.encrypt(passwd)
        userInfos = {'user':user,'password':passwd}
        sql.addNewUser(userInfos) #写库
    except MyException,e:
        print e
        return False
    print u"注册成功，用户名 : %s " % (user)
    return True


if __name__ == '__main__':
    apply()


