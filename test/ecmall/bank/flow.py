#!/usr/bin/env python
#coding:utf8
import sqlOperator as sql
import  re,time,login,decimal,utils
"""
    银行消费流水记录
    查看流水日志，查看流水，打印流水等操作
    author ： flybird1971
    since  : 2015-11-02 12:23:44
"""

def writeFlow(cardNo,money):
    """
    流水
    """
    data = {}
    data['cardNo'] = cardNo
    data['type'] = 'debit' if decimal.Decimal(money) <0 else 'credit'
    data['money'] = money
    if not sql.writeFlow(data):
        print u"流水记录失败"
        return False
    return  True

def debitFlow(cardNo,money):
    """
    借方流水
    """
    money = decimal.Decimal(0)- decimal.Decimal(money)
    if not writeFlow(cardNo,str(money)):return  False
    return  True

def creditFlow(cardNo,money):
    """
    贷方流水:
    """
    if not writeFlow(cardNo,str(money)):return False
    return True

def readFlow():
    """
    读取流水记录
    """
    cardNo = sql.readLoginCardNo()
    if not  cardNo:
        print u"请先登录..."
        login.loginStart()
        cardNo = sql.readLoginCardNo()
    result = sql.readFlow(cardNo)
    if not result:return []
    return result

def readTime():
    """
    读取年月日数据
    """
    while True:
        year = raw_input(u"输入查询年,格式2002 或q退出：")
        if year =='q' :return False
        regexYear = re.compile(r'[1,2]0[\d]{2}')
        if not regexYear.match(year):
            print u"输入年份格式错误，"
            continue
        break;

    while True:
        month = raw_input(u"输入查询月份,格式01 | 11 或q退出：")
        if month =='q' :return False
        monthYear = re.compile(r'(([0][1-9])|(1[0-2]))')
        if not monthYear.match(month):
            print u"输入月份格式错误，"
            continue
        break;

    while True:
        day = raw_input(u"输入查询日期,格式01 | 21 |31 或q退出：")
        if day =='q' :return False
        dayYear = re.compile(r'(([0][1-9])|([12][0-9])|(3[01]))')
        if not dayYear.match(day):
            print u"输入日期格式错误，"
            continue
        break;
    return "%s-%s-%s 00:00:00" % (year,month,day)

def readFlowByCondition():
    """
    根据时间段读取流水记录
    """
    cardNo = sql.readLoginCardNo()
    if not  cardNo:
        print u"请先登录..."
        login.loginStart()
        cardNo = sql.readLoginCardNo()

    print u"请输入查询开始时间："
    beginTime = readTime()
    if not beginTime:return False

    print u"请输入查询结束时间："
    endTime = readTime()
    if not endTime:return False

    beginTime = int(time.mktime(time.strptime(beginTime,'%Y-%m-%d %H:%M:%S')))
    endTime = int(time.mktime(time.strptime(endTime,'%Y-%m-%d %H:%M:%S')))
    result = sql.readFlow(cardNo,beginTime,endTime)
    if not result:return []
    return result

flowService = [{u'按日期拉取流水记录':readFlowByCondition},
             {u'拉取所有流水记录':readFlow}]
def show():
    print u"\n\n\n +++++++++++++你已经进入流水相关服务 ：  +++++++++++++"
    cardNo = sql.readLoginCardNo()
    if not  cardNo:
        print u"请先登录..."
        login.loginStart()
        cardNo = sql.readLoginCardNo()

    while True:
        utils.printTable(flowService)
        num =  raw_input(u"请选择对应服务 或者 输入q退出 ：")
        if num == 'q': break
        regex = re.compile(r"\d+")
        if (not regex.match(num))  or (  int(num) >= len(flowService)):
            print u"请输入正确服务号码"
            continue
        num = int(num)
        break
    result = flowService[num].values().pop()()
    if not result :
        print u"无任何记录"
        return True

    for t in result:
        tmpDict = {'type':t.get('type'),'money':t.get('money')}
        tmpDict['time'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t.get('time')))
        print tmpDict
    return  True

if __name__ =="__main__":
    show()

