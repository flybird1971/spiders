#!/usr/bin/env python
#coding:utf8
"""
    用户支付逻辑
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""
import car,decimal
import sqlOperator as sql
import sys,os
sys.path.insert(1,os.path.realpath('..'))
import bank.pay as uPay
import shopAdmin.config as config

def pay():
    goodsInfos = sql.readCars() #读取购物车商品信息
    money = 0.00
    #计算待支付金额
    for tmp in goodsInfos:
        money = decimal.Decimal(money) + decimal.Decimal(tmp.get('price'))*decimal.Decimal(tmp.get('num'))
    car.viewCard() #打印要支付商品
    print u"共计 %s 元 " % (money)

    if decimal.Decimal(money) <= 0:
        print u"不用支付"
        return False

    configData = config.readConfig()
    cardNo = configData.get('cardNo')
    if not uPay.pay(cardNo,money): #网银支付
        print u"支付失败"
        return False
    sql.sysGoods() #将购物车商品同步到已购商品中心，并减少库存
    return True

if __name__=='__main__':
    pay()