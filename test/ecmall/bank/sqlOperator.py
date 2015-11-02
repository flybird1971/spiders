#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from MyException import MyException

"""
    银行数据操作  模拟sql
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""

path = '../data/bank_user'
def writeData(userinfo):
    """
    申请银行卡成功后，用户信息写库
    """
    f = None
    try:
        f = open(path,'ab+')
        f.write(json.dumps(userinfo) + "\n")
    except IOError:
        raise MyException,"数据入库失败"
    finally:
        f.close()
    return True

def readUserInfos(indexKey,value):
    """
    根据key，cardno or idcard读取用户信息
    """
    userInfos = []
    with open(path,'rb') as f:
        for line in f.xreadlines():
            userDict = json.loads(line)
            if userDict.get(indexKey) == value :
                userInfos.append(userDict)
    return userInfos

def getUserInfosByCarNo(cardNo):
    """
    根据卡号读取用户信息
    """
    cardList = readUserInfos('cardNo',cardNo)
    if len(cardList) < 1:return {}
    return cardList.pop()

def isExists(idCard):
    """
    检测身份证号是否申请过银行卡
    """
    return readUserInfos('idCard',idCard)

def showOldCard(idCard):
    """
    打印之前申请过的银行卡号
    """
    oldCards = isExists(idCard)
    if oldCards :
        print u"你之前申请过银行卡 ： "
        for tmp in oldCards:
            print u"\t\t 卡号 ：%s " % (tmp['cardNo'])
        isNext = raw_input(u"你是否继续申请银行卡（y or n） ： ")
        if isNext == 'n':
            raise MyException,"退出注册"
    return True

def markLoginSuccess(cardNo):
    """
    记录登录状态
    """
    with open('../data/login_user','w+') as f:
        f.write(cardNo)
    return True
