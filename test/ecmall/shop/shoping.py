#!/usr/bin/env python
#coding:utf8
import sqlOperator as sql
import car
import  pay
import sys,os
sys.path.insert(1,os.path.realpath('..'))
import shopAdmin.good as goods
import shopAdmin.sqlOperator as goodsSql
"""
    用户购物操作
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""
def listGoods():
    goods.listGoods()

def show():
    while True:
        print u"\n*************请选择商品****************\n"
        listGoods()
        goodsId = raw_input(u"请输入要购买商品id 或者q退出 ： ")
        if goodsId=='q':return False
        goodsInfo = goodsSql.getGoodsInfosById(goodsId)
        if not goodsInfo :
            print u"你选择的商品不存在"
            isGo = raw_input(u"是否继续购物 y or n ")
            if isGo=='n' :return False
            continue
        car.addGoods(goodsInfo)
        isGo = raw_input(u"是否继续购物 y or n ")
        if isGo=='n' :return False
        continue
    return True


if __name__=='__main__':
    show()
    # isPay = raw_input( u"是否到支付中心进行付款 y or n: ")
    # if isPay=='n':return False
    # pay.pay()