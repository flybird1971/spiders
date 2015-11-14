#!/usr/bin/env python
#coding:utf8
import sqlOperator as sql
import login
import sys,os
sys.path.insert(1,os.path.realpath('..'))
import bank.utils as utils
"""
    商城购物车，查看购物车，已支付商品修改购物车中商品状态等逻辑
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""
def addGoods(goodsInfos):
    goodsInfos['num'] = 1
    return sql.updateCars(goodsInfos)

def delGoods():
    isShow = raw_input(u"是否查看购物车中商品 y or n")
    if isShow=='y':
        viewCard()
    goodsId = raw_input( u"请输入你要删除商品id或者q退出 :")
    if goodsId=='q':return False
    return  sql.delCars(goodsId,True)

def viewCard():
    goodsList = sql.readCars()
    if not goodsList:
        print u"购物车无商品"
        return False
    return  utils.printGoods(goodsList)

def viewMyGoods():
    goodsList = sql.readMyGoods(sql.readLoginUser())
    if not goodsList :
        print u"无已支付商品"
        return  False
    return utils.printGoods(goodsList)


seviceCars = [{u'查看购物车':viewCard},{u'删除购物车中商品':delGoods},{u'查看已付款商品':viewMyGoods}]
def show():
    print u"\n\n\n +++++++++++++你已经进入商城购物车中心 ：  +++++++++++++"
    username = sql.readLoginUser()
    if not  username:
        while True:
            print u"请先登录..."
            login.loginStart()
            username = sql.readLoginUser()
            if not username :
                mark = raw_input(u"是否继续登录y or n")
                if mark=='n':return  False
                continue
            break

    num = utils.printTableX(seviceCars)
    if num == -1:return False
    result = seviceCars[num].values().pop()()
    return  True

if __name__=='__main__':
    show()
