#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json,re,sys
import utils
from MyException import MyException
import sqlOperator as sql

"""
    银行卡申请业务逻辑处理
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""

def readIDcard():
    """
    读入用户身份证号，并进行检测是否合法
    """
    idCard = None
    while True:
        id = raw_input(u"请输入你身份证号 或者 输入q退出 : ")
        if id == 'q':
            raise MyException,"logout....."
        regex = re.compile(r'\d{16,18}')
        if not regex.match(id):
            print u"warn : 你输入的身份证号格式不正确，请重新输入 或者 输入q退出 ！"
            continue
        idCard = id
        break
    return idCard

def readPasswd():
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
    申请银行卡
    """
    print u"\n\n\n +++++++++++++你已经进入注册相关服务 ： +++++++++++++ "
    try:
        idCard = readIDcard() #读入用户输入身份证号，并验证身份证号是否合法
        sql.showOldCard(idCard)   #检测身份证号是否已经申请过卡号
        passwd = readPasswd() #输入密码
        passwd = utils.encrypt(passwd)
        cardNo = utils.uniqueNo() #生成卡号
        sql.writeData({'cardNo':cardNo,'idCard':idCard,'password':passwd,'money':0}) #写库
    except MyException,e:
        print e
        return False
    except IOError:
        print u"文件不存在 : "
        return False
    print u"申请成功，银行卡号 : %s " % (cardNo)
    return True


if __name__ == '__main__':
    apply()


