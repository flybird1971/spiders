#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json,os,decimal,time
from MyException import MyException
import flow

"""
    银行数据操作  模拟sql
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""

path = os.getcwd()+'/data/bank_user'
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

def updateData(cardNon,data):
    """
    更新用户数据
    """
    try:
        fw = open(path+".tmp",'wb+')
        fr = open(path,'rb+')
        for line in fr.xreadlines():
            try:
                userDict = json.loads(line)
                if userDict.get('cardNo') == cardNon :
                    for field in data:
                        userDict[field] = data[field]
                line = json.dumps(userDict)
                fw.write(line+"\n")
            except ValueError,e:
                continue
    except IOError:
        raise MyException,'file error'
    finally:
        fw.close()
        fr.close()
    os.remove(path)
    os.rename(path+'.tmp',path)
    return True


def readUserInfos(indexKey,value):
    """
    根据key，cardno or idcard读取用户信息
    """
    userInfos = []
    with open(path,'rb') as f:
        for line in f.xreadlines():
            try:
                userDict = json.loads(line)
                if userDict.get(indexKey) == value :
                    userInfos.append(userDict)
            except ValueError,e:
                print line
                continue
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


def updateMoney(cardNo,money):
    """
    更新账户余额
    """
    userDict = getUserInfosByCarNo(cardNo)
    oldMoney = userDict.get('money',0)
    newMoney = decimal.Decimal(oldMoney)+decimal.Decimal(money)
    newMoney = round(decimal.Decimal(newMoney),2)
    if newMoney < 0.00:
        print u"余额不足"
        return False

    if not updateData(cardNo,{'money':newMoney}):
        print u"更新金额失败"
        return False

    #写流水
    if decimal.Decimal(money) > 0:
       flow.creditFlow(cardNo,abs(decimal.Decimal(money)))
    else:
       flow.debitFlow(cardNo,abs(decimal.Decimal(money)))

    print u"账号 %s 成功存储 %s 元,共计%s元 " % (cardNo,money,str(newMoney))
    return True

def transferMoney(debitCardNo,creditCardNo,money):
    """
    转账数据接口
    debitCardNo  借方账户  金额减少
    creditCardNo 贷方账户  金额增多
    """
    debitUserDict = getUserInfosByCarNo(debitCardNo)
    creditUserDict = getUserInfosByCarNo(creditCardNo)

    debitAccount = debitUserDict.get('money',0)
    creditAccount = creditUserDict.get('money',0)

    if decimal.Decimal(debitAccount) - decimal.Decimal(money) < 0 :
        print u"借方%s 余额不足" % (creditCardNo)
        return False

    debitNewMoney = decimal.Decimal(debitAccount) - decimal.Decimal(money)
    debitNewMoney = round(debitNewMoney,2)
    creditNewMoney = decimal.Decimal(creditAccount) + decimal.Decimal(money)
    creditNewMoney = round(creditNewMoney,2)

    if not updateData(debitCardNo,{'money':debitNewMoney}) :
        print u"更新金额失败"
        return False
    if not updateData(creditCardNo,{'money':creditNewMoney}):
        print u"更新金额失败"
        updateData(debitCardNo,{'money':debitAccount})
        return False

    flow.creditFlow(creditCardNo,abs(decimal.Decimal(money)))
    flow.debitFlow(debitCardNo,abs(decimal.Decimal(money)))

    print u"账号 %s 成功转入 %s 元,共计%s元 " % (creditCardNo,money,str(creditNewMoney))
    print u"账号 %s 成功转出 %s 元,共计%s元 " % (debitCardNo,money,str(debitNewMoney))
    return True

markPath = os.getcwd()+'/data/login_user'
def markLoginSuccess(cardNo):
    """
    记录登录状态
    """
    # with open('../data/login_user','w+') as f:
    with open(markPath,'w+') as f:
        f.write(cardNo)
    return True

def readLoginCardNo():
    """
    获取当前登录的卡号
    """
    with open(markPath,'rb') as f:
        cardNo = f.read()
    if not cardNo: return False
    return cardNo


##########################################################
###  流水
##########################################################

flowPath =os.getcwd()+ '/data/bank_flow'

def writeFlow(data):
    """
    插入流水记录
    """
    f = None
    try:
        f = open(flowPath,'ab+')
        data['time'] = int(time.time())
        f.write(json.dumps(data) + "\n")
    except IOError:
        raise MyException,"数据入库失败"
    finally:
        f.close()
    return True

def readFlow(cardNo,beginTime=None,endTime=None):
    """
    读取流水记录
    """
    if beginTime== None or endTime==None or int(beginTime)>int(endTime):
        beginTime = None
        endTime = None

    result = []
    with open(flowPath,'rb+') as f:
        for line in f.xreadlines():
            try:
                flow = json.loads(line)
                if flow.get('cardNo') != cardNo:continue #卡号一致跳过
                time = int(flow.get('time'))
                if beginTime != None and (time < beginTime or time>endTime):continue
                result.append(flow)
            except ValueError,e:
                continue
    return result



