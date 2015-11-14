#!/usr/bin/env python
#coding:utf8
import  sqlOperator as sql
import login
import sys,os,re
sys.path.insert(1,os.path.realpath('..'))
import bank.utils as utils
import bank.sqlOperator as cardSql

"""
    商城银行卡号配置
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""
def readConfig():
    configData = sql.readConfig()
    for tmp in configData:
        print tmp

def setConfig(data):
    return sql.setConfig(data)

def setShopCard():
    cardNo = raw_input(u"请输入银行卡号 或者q退出：")
    if cardNo=='q':return  False
    if not cardSql.getUserInfosByCarNo(cardNo):
        print u"卡号未在银行开户"
        return False
    config = {'cardNo':cardNo}
    return setConfig(config)

def inputUser():
    """
    输入用户名
    """
    while True:
        user = raw_input(u"请输入管理员用户名 或者 q退出：")
        if user=='q':return False
        regexUser = re.compile(r'\w{6,12}')
        if not regexUser.match(user):
            print u"用户名必须6-12位，只能是字母，数字，下划线"
            continue
        break
    return user

def inputPasswd():
    while True:
        passwd = raw_input(u"请输入密码 或者 q退出：")
        if passwd =='q':return  False
        regexPwd = re.compile(r'\w{6,15}')
        if not regexPwd.match(passwd):
            print u"用户名必须6-12位，只能是字母，数字，下划线"
            continue
        break
    return passwd

def setAdminUserAndPwd():
    user = inputUser()
    if not user:return False

    passwd = inputPasswd()
    if not passwd:return  False
    passwd = utils.encrypt(passwd)
    config = {"admin":{'user':user,'password':passwd}}
    return setConfig(config)

seviceConfig = [{u'配置银行卡':setShopCard},{u"配置管理员账户":setAdminUserAndPwd}]
def show():
    print u"\n\n\n +++++++++++++你已经进入商城后台配置相关服务 ：  +++++++++++++"
    username = sql.isLogin()
    if not  username:
        while True:
            print u"请先登录..."
            login.loginStart()
            username = sql.isLogin()
            if not username :
                mark = raw_input(u"是否继续登录y or n")
                if mark=='n':return  False
                continue
            break

    num = utils.printTableX(seviceConfig)
    if num == -1:return False
    result = seviceConfig[num].values().pop()()
    return  True

if __name__=='__main__':
    show()