#!/usr/bin/env python
#coding:utf8
import  sqlOperator as sql
import login
import sys,os,re
sys.path.insert(1,os.path.realpath('..'))
import bank.utils as utils
"""
    商城商品添加，删除
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""

def inputPrice():
    while True:
        goodsPrice = raw_input(u"请输入商品价格 或者q退出：")
        if goodsPrice=='q':return False
        regexPrice = re.compile(r'((\d+)|(\d+\.\d+)|(0\.\d+))')
        if not regexPrice.match(goodsPrice):
            print u"商品价格格式错误，请重新输入"
            continue
        break
    return goodsPrice

def inputNum():
    while True:
        goodsNum = raw_input(u"请输入添加商品件数 或者q退出：")
        if goodsNum=='q':return False
        regexNum = re.compile(r'\d+')
        if not regexNum.match(goodsNum):
            print u"添加商品件数格式错误，请重新输入"
            continue
        break
    return goodsNum

def addGoods():
    goodsName = raw_input(u"请输入商品名称：")
    goodsType = raw_input(u"请输入商品类别：")
    goodsPrice = inputPrice()
    if not goodsPrice:return  False
    goodsNum = inputNum()
    if not goodsNum:return  False

    goodsInfo = {'name':goodsName,'type':goodsType,'price':goodsPrice,'num':goodsNum}
    sql.writeData(goodsInfo)
    return True

def listGoods():
    goodsInfos = sql.readGoods()
    utils.printGoods(goodsInfos)
    return True

def updateGoods():
    isList = raw_input(u"是否要列出所有商品 y or n")
    if isList=='y':
        listGoods()
    id = raw_input(u"请选择要更新商品id:")
    regexId = re.compile(r'\d+')
    if not sql.getGoodsInfosById(id):
        print u"你选择的商品不存在"
        return False

    goodsName = raw_input(u"请输入商品名称：")
    goodsType = raw_input(u"请输入商品类别：")
    goodsPrice = inputPrice()
    if not goodsPrice:return  False
    goodsNum = inputNum()
    if not goodsNum:return  False

    goodsInfo = {'name':goodsName,'type':goodsType,'price':goodsPrice,'num':goodsNum}
    if not sql.updateData(id,goodsInfo):
        print u"更新失败"
        return False
    print u"更新成功"
    return True

def delGoods():
    isList = raw_input(u"是否要列出所有商品 y or n")
    if isList=='y':
        listGoods()
    id = raw_input(u"请选择要删除商品id:")
    regexId = re.compile(r'\d+')
    if not sql.getGoodsInfosById(id):
        print u"你选择的商品不存在"
        return False
    sql.delData(id)
    return True

goodsService = [{u'查看商品列表':listGoods},{u'添加商品':addGoods},{u'更新商品':updateGoods},{u'删除商品':delGoods}]
def show():
    print u"\n\n\n +++++++++++++你已经进入商城后商品操作中心 ：  +++++++++++++"
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

    num = utils.printTableX(goodsService)
    if num == -1:return False
    result = goodsService[num].values().pop()()
    return  True

if __name__=="__main__":
    show()