#!/usr/bin/env python
#coding:utf8
import utils
import sqlOperator as sql
"""
    用户登录银行操作
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""
def login(cardNo,passwd):
    userInfos = sql.getUserInfosByCarNo(cardNo)
    if not userInfos:
        return False
    if userInfos['password'] != utils.encrypt(passwd):
        return False
    sql.markLoginSuccess(cardNo)
    print u"登录成功"
    return True

def loginStart():
    print u"\n\n\n +++++++++++++你已经进入登录相关服务 ： +++++++++++++ "
    while True:
        cardNo = raw_input(u"输入银行卡号 或者 输入q退出登录：")
        if cardNo == 'q':return False
        passwd = raw_input(u"输入密码 或者 输入q退出登录 ：")
        if passwd == 'q':return False
        if not login(cardNo,passwd):
            print u"卡号或者密码错误，请重新登录 "
            continue
        break
    return True

if __name__ == "__main__":
    loginStart()

