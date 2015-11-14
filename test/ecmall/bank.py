#!/usr/bin/env python
#coding:utf8
from bank import register
from bank import login
from bank import resetpwd
from bank import pay
from bank import saveMoney
from bank import getMoney
from bank import flow
from bank import utils
import re
"""
    银行入口
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""

service = [{u'注册':register.apply},
           {u'登录':login.loginStart},
           {u'重置密码':resetpwd.resetPwd},
           {u'第三方支付接口':pay.pay},
           {u"存款":saveMoney.saveMoney},
           {u"取款":getMoney.getMoney},
           {u"流水":flow.show}]


def index():
    """银行相关操作入口
    """
    while True:
        utils.printTable(service)
        num =  raw_input(u"请选择对应服务 或者 输入q退出 ：")
        if num == 'q': break

        regex = re.compile(r"\d+")
        if (not regex.match(num))  or (  int(num) >= len(service)):
            print u"请输入正确服务号码"
            continue
        num = int(num)
        service[num].values().pop()()
        isNext = raw_input(u"是否继续选择其他服务：y or n")
        if isNext != 'y':
            break
        print u"\n\n************************* 服务主界面 *******************************\n"
    print u"------------- end -------------"
    return True



if __name__=='__main__':
    index()