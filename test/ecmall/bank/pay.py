#!/usr/bin/env python
#coding:utf8
import sqlOperator as sql
import login,re
"""
    第三方支付业务操作
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""
def inputMoney():
    """
    输入存储金额
    """
    while True:
        money = raw_input(u"请输入要存款金额 或者 输入q退出: ")
        if money=='q':return False
        regex = re.compile(r'^(([1-9][\d]*)|(0\.\d{1,2})|([1-9]\d*\.\d{1,2}))$')
        if not regex.match(money):
            print u"金额不正确,必须是数字，且要大于0"
            continue
        return money

def inputCardNoAndPwd():
    cardNo = raw_input(u"请输入卡号:")
    passwd = raw_input(u"请输入密码 :")
    if not login.login(cardNo,passwd):
        print u"卡号或者密码错误"
        return False
    return cardNo

def inputCreditCardNo():
    cardNo = raw_input(u"请输入转账卡号:")
    card = sql.getUserInfosByCarNo(cardNo)
    if not card :
        print (u"你输入待转账卡号不存在")
        return False
    return cardNo

def sysAccount(debitCardNo,creditCardNo,money):
    """
    debit  借方 金额减少
    credit 贷方 金额增多
    """
    return sql.transferMoney(debitCardNo,creditCardNo,money)


def pay(creditCardNO=False,money=False):
    print u"\n\n\n +++++++++++++你已经进入第三方支付相关服务 ： +++++++++++++"
    debitCardNo = inputCardNoAndPwd()
    if not debitCardNo :return False

    if not money:
        money = inputMoney()
    if not money: return False

    if not creditCardNO:
        creditCardNO = inputCreditCardNo()
    if not creditCardNO :return  False

    if not sysAccount(debitCardNo,creditCardNO,money):
        print u"转账失败"
        return False
    print u"转账成功"
    return True

if __name__=='__main__':
    pay()

