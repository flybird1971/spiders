#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json,os,sys
sys.path.insert(1,os.path.realpath('..'))
from MyException.MyException import MyException

"""
    商城后台配置，商品添加删除等 数据操作  模拟sql
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""
goodsIdPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/shop_goods_max_id'))
def getMaxId():
    """
    获取当前商品最大id
    """
    with open(goodsIdPath,'r') as f:
        max = f.read()
    if not max :return 0
    return max

def updateMaxId(id):
    """
    更新商品最大Id
    """
    with open(goodsIdPath,'w+') as f:
        f.write(str(id))
    return True

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/shop_goods'))
def writeData(goodsInfos):
    """
    商品添加相关操作
    """
    maxId = getMaxId()
    goodsInfos['id'] = int(maxId)+1
    f = None
    try:
        f = open(path,'ab+')
        f.write(json.dumps(goodsInfos) + "\n")
    except IOError:
        raise MyException,"数据入库失败"
    finally:
        f.close()
    updateMaxId(int(maxId)+1)
    return True

def updateData(goodsId,data):
    """
    更新商品数据
    """
    print "update............."
    try:
        fw = open(path+".tmp",'wb+')
        fr = open(path,'rb+')
        for line in fr.xreadlines():
            try:
                goodsInfo = json.loads(line)
                if str(goodsInfo.get('id')) == str(goodsId) :
                    for field in data:
                        goodsInfo[field] = data[field]
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

def decreaseGoods(goodsId,num):
    """
    更新商品库存
    """
    print "update............."
    try:
        fw = open(path+".tmp",'wb+')
        fr = open(path,'rb+')
        for line in fr.xreadlines():
            try:
                goodsInfo = json.loads(line)
                if str(goodsInfo.get('id')) == str(goodsId) :
                    goodsInfo['num'] = int(goodsInfo['num']) - num
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


def delData(goodsId):
     """
        删除商品数据
     """
     try:
        fw = open(path+".tmp",'wb+')
        fr = open(path,'rb+')
        for line in fr.xreadlines():
            try:
                goodsInfo = json.loads(line)
                if str(goodsInfo.get('id')) == str(goodsId):
                    continue
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

def readGoods():
    """
    读取商品信息
    """
    goodsInfos = []
    with open(path,'rb') as f:
        for line in f.xreadlines():
            try:
                goodsDict = json.loads(line)
                goodsInfos.append(goodsDict)
            except ValueError,e:
                print line
                continue
    return goodsInfos

def readGoodsInfos(indexKey,value):
    """
    根据key，goodsId or goodType读取商品信息
    """
    goodsInfos = []
    with open(path,'rb') as f:
        for line in f.xreadlines():
            try:
                goodsDict = json.loads(line)
                if str(goodsDict.get(indexKey)) == str(value):
                    goodsInfos.append(goodsDict)
            except ValueError,e:
                print line
                continue
    return goodsInfos

def getGoodsInfosById(goodsId):
    """
    根据商品id读取商品信息
    """
    goodsList = readGoodsInfos('id',goodsId)
    if len(goodsList) < 1:return {}
    return goodsList.pop()

def getGoodsInfosByType(goodsType):
    """
    根据商品类型拉取商品信息
    """
    return readGoodsInfos('type',goodsType)

##########################################################
###  商城后台登录标记
##########################################################
markPath = configPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/shop_admin_login'))
def markLoginSuccess(user):
    with open(markPath,'w+') as f:
        f.write(user)
    return True

def isLogin():
    with open(markPath,'r') as f:
        user = f.read()
    return user

##########################################################
###  商城配置
##########################################################
# configPath = os.getcwd()+'/data/login_user'
# configPath = os.getcwd()+'/data/shop_config'
configPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/shop_config'))
def readConfig():
    """
    读取商品配置
    """
    with open(configPath,'rb') as f:
        configData = f.read()
    if not configData: return {}
    return json.loads(configData)

def setConfig(configData):
    """
    设置商品配置
    """
    oldConfigData = readConfig()
    for tmp in configData :
        oldConfigData[tmp] = configData[tmp]

    with open(configPath,'w+') as f:
        f.write(json.dumps(oldConfigData))
    return True




