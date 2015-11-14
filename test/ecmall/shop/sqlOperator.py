#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json,os,decimal,time,sys
sys.path.insert(1,os.path.realpath('..'))
from MyException.MyException import MyException

"""
    商城购物数据操作  模拟sql
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/shop_car'))
def writeData(goodsInfos):
    """
    添加商品到购物车
    """
    f = None
    try:
        f = open(path,'ab+')
        f.write(json.dumps(goodsInfos) + "\n")
    except IOError:
        raise MyException,"数据入库失败"
    finally:
        f.close()
    return True

def updateCarsByGoodsId(goodsId):
    try:
        fw = open(path+".tmp",'wb+')
        fr = open(path,'rb+')
        for line in fr.xreadlines():
            try:
                goodsInfo = json.loads(line)
                if str(goodsInfo.get('id')) == str(goodsId) :
                        goodsInfo['num'] = int(goodsInfo['num']) + 1
                line = json.dumps(goodsInfo)
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

def updateCars(goodsInfo):
    print "update............."
    if not getByGoodsId(goodsInfo.get('id')):
        return writeData(goodsInfo)
    return updateCarsByGoodsId(goodsInfo.get('id'))

def delCars(goodsId,isAll=False):
    try:
        fw = open(path+".tmp",'wb+')
        fr = open(path,'rb+')
        for line in fr.xreadlines():
            try:
                goodsInfo = json.loads(line)
                if str(goodsInfo.get('id')) == str(goodsId) :
                        if isAll:continue
                        goodsInfo['num'] = int(goodsInfo['num']) - 1
                        if int(goodsInfo['num']) <=0 :continue
                line = json.dumps(goodsInfo)
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

def readCars():
    """
    读取购物车
    """
    goodsInfos = []
    with open(path,'rb') as f:
        for line in f.xreadlines():
            try:
                goodsDict = json.loads(line)
                goodsInfos.append(goodsDict)
            except ValueError,e:
                continue
    return goodsInfos

def getByGoodsId(goodsId):
    """
    查找购物车中是否有某商品
    """
    goodsInfos = []
    with open(path,'rb') as f:
        for line in f.xreadlines():
            try:
                goodsDict = json.loads(line)
                if str(goodsDict.get('id')) == str(goodsId):
                    return goodsDict
            except ValueError,e:
                continue
    return goodsInfos


##########################################################
###  同步购物车商品到已购商品中心，并减少库存
##########################################################
sys.path.insert(1,os.path.realpath('..'))
import shopAdmin.sqlOperator as goodsSql
def sysGoods():
    goodsList = readCars()
    for goods in goodsList:
        goodsSql.decreaseGoods(goods.get('id'),goods.get('num'))
        updateMyGoods(goods)
        delCars(goods.get('id'),True)
    return True



##########################################################
###  已买商品存储
##########################################################

myGoodsPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/my_goods'))

def updateMyGoods(data):
    """
    插入已经购物商品记录
    """
    f = None
    try:
        f = open(myGoodsPath,'ab+')
        data['time'] = int(time.time())
        data['user'] = readLoginUser()
        f.write(json.dumps(data) + "\n")
    except IOError:
        raise MyException,"数据入库失败"
    finally:
        f.close()
    return True

def readMyGoods(user,beginTime=None,endTime=None):
    """
    读取流水记录
    """
    if beginTime== None or endTime==None or int(beginTime)>int(endTime):
        beginTime = None
        endTime = None

    result = []
    with open(myGoodsPath,'rb+') as f:
        for line in f.xreadlines():
            try:
                flow = json.loads(line)
                if flow.get('user') != user:continue #卡号一致跳过
                time = int(flow.get('time'))
                if beginTime != None and (time < beginTime or time>endTime):continue
                result.append(flow)
            except ValueError,e:
                continue
    return result






##########################################################
###  判断商城用户注册
##########################################################
shopUserPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/shop_user'))
def addNewUser(userinfo):
    """
    用户信息写库
    """
    f = None
    try:
        f = open(shopUserPath,'ab+')
        f.write(json.dumps(userinfo) + "\n")
    except IOError:
        raise MyException,"数据入库失败"
    finally:
        f.close()
    return True

def updateUser(user,data):
    """
    更新用户数据
    """
    try:
        fw = open(shopUserPath+".tmp",'wb+')
        fr = open(shopUserPath,'rb+')
        for line in fr.xreadlines():
            try:
                userDict = json.loads(line)
                if userDict.get('user') == user :
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
    os.remove(shopUserPath)
    os.rename(shopUserPath+'.tmp',shopUserPath)
    return True

def readUserInfos(indexKey,value):
    """
    根据key，cardno or idcard读取用户信息
    """
    userInfos = []
    with open(shopUserPath,'rb') as f:
        for line in f.xreadlines():
            try:
                userDict = json.loads(line)
                if userDict.get(indexKey) == value :
                    userInfos.append(userDict)
            except ValueError,e:
                print line
                continue
    return userInfos

def getUser(user):
    result = readUserInfos('user',user)
    if not result :return False
    return result.pop()




##########################################################
###  判断商城用户是否登录
##########################################################
markPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/shop_login'))
def markLoginSuccess(user):
    """
    记录登录状态
    """
    with open(markPath,'w+') as f:
        f.write(user)
    return True

def readLoginUser():
    """
    获取当前登录用户名
    """
    with open(markPath,'rb') as f:
        user = f.read()
    if not user: return False
    return user



