#!/usr/bin/env python
#coding:utf8
import sqlOperator as sql
import login,re
"""
    用户存款操作
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

def saveMoney():
    """
    存款
    """
    print u"\n\n\n +++++++++++++ 你已经进入存款相关服务 ：++++++++++++++++++++ "
    cardNo = sql.readLoginCardNo()
    if not  cardNo:
        print u"请先登录..."
        login.loginStart()
        cardNo = sql.readLoginCardNo()
    money = inputMoney()
    if not money:return False
    sql.updateMoney(cardNo,money)


if __name__=='__main__':
    saveMoney()