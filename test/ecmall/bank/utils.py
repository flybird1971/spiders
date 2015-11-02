#!/usr/bin/env python
#coding:utf8
import hashlib,random,time

"""
工具函数
"""

def encrypt(str):
    """
    用于注册用户加密
    """
    hash = hashlib.md5()
    hash.update(str)
    return hash.hexdigest()

def uniqueNo():
    """
    生成银行卡号
    """
    cardNo = []
    for t in xrange(18):
        cardNo.append(str(random.randint(0,9)))
    return ''.join(cardNo)