#encoding:utf8
__author__ = 'flybird1971'
import  random

#生成随机字符串
def randStr(length,chars=None):
    if not chars :
        chars = '0123456789abcdefghijklmnopqrstuvw'
        chars += 'xyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max = len(chars)
    result = ''
    timer = 0
    while timer<length:
        index = random.randint(0,max-1)
        result += chars[index]
        timer += 1
    return result





#屏蔽被调用时，不执行部分操作
if(__name__ == '__main__'):
   print randStr(12,'123454abc%&*')

