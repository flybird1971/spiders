#!/usr/bin/env python
#coding:utf8
import sqlOperator as sql
import login
import register
import utils
from MyException import  MyException
"""
    重置银行卡密码处理
    安全考虑，重置密码前一定要重新登录
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""

def resetPwd():
    """
    重置密码
    """
    print u"\n\n\n +++++++++++++你已经进入重置密码相关服务 ：+++++++++++++ "
    if not login.loginStart():
        print (u"登录失败，不能重置密码")
        return False

    try:
        print (u"---------------重置密码-----------------")
        passwd = register.readPasswd() #输入新密码
        passwd = utils.encrypt(passwd)
        cardNo = sql.readLoginCardNo()
        sql.updateData(cardNo,{'password':passwd}) #更新数据
    except MyException,e:
        print e
        return False
    print u"密码重置成功"
    return True


if __name__ == "__main__":
    resetPwd()