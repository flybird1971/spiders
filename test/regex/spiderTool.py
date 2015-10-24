#coding:utf8
import socket
import re as regex
import urllib2
import json
import os
import countTimes
import time
__author__ = 'flybird1971'

#存放所有被处理过的url
urlSpidered = {}

#失败url
badUrl = {}

#抓取网站域名
domain = 'http://www.guonainai.com'

#socket 超时时间设置
timeout = 20

#根据url，载入网页文本数据
def getHtml(url):
    print "loading "+url+" ......."
    try:
        html = urllib2.urlopen(url,timeout=timeout)
    except urllib2.URLError,e:
        print "Bad URL : "+url+"  or timeout"
        badUrl[url] = True
        return None
    except socket.timeout,e:
        print "socket timeout url : "+url
        badUrl[url] = True
        return None

    try:
        content = html.read()
    except socket.timeout,e:
        print "html read ,,, socket timeout url : "+url
        badUrl[url] = True
        return None

    print "load is over !  url : "+url
    return content

#根据载入的网页文本，匹配url地址
def getUrl(content):
    print "pasring ..... "
    if not content:
        print "pase url is over ! "
        return None
    urlReg  = regex.compile(r'(src|href)=["\'](.+?)["\']',regex.I)
    urlList = urlReg.findall(content)
    print "pase url is over ! "
    return urlList

#过滤指定链接
#  eg : css js jgp png jpeg gif ico等文件
def filter(urlList,pattern=None):
    print "filter starting....."
    if not urlList:
        print "filter is over ! "
        return None
    if not pattern:
        pattern = r'(.+(com|cn|net|org)\/?$)|([\/\/\#])|(.+(gif|jpeg|jpg|png|css|js|ico|xml)(\?.+)?)$'
    filterReg = regex.compile(pattern,regex.I)
    result = []
    tupleTmp = ()
    for tupleTmp in urlList :
        if  filterReg.match(tupleTmp[1]) :
            continue
        if urlSpidered.get(tupleTmp[1]) or badUrl.get(tupleTmp[1]):
            continue
        urlSpidered[tupleTmp[1]] = True
        result.append(tupleTmp[1])
        print tupleTmp[1]
    print "filter is over ! "
    return result

# 递归抓取网页时，
# 过滤获得的url中不是本域名,不用于递归
# url没有域名时，追加域名组成完整url
def sureDomain(urlList,domain,pattern=None):
    print "sure domain starting ...."
    if not domain :
        return False
    if not pattern:
        pattern = r'^('+domain+')'
        sureRegex = regex.compile(pattern,regex.I)
        appenDomainPattern = r'^[\/\\]'
        appenDomainRegex = regex.compile(appenDomainPattern,regex.I)
    result = []
    tmpUrl = ''
    for tmpUrl in urlList:
        if sureRegex.match(tmpUrl):
            result.append(tmpUrl)
        if appenDomainRegex.match(tmpUrl):
            result.append(domain+tmpUrl)
    print "sure domain end !!!"
    print json.dumps(result)
    return result

#写盘
def flashFile(data,path):
    file = open(path,'wb')
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    file.write(json.dumps([now,data]))
    print "flash data >>> badUrl : %d  <<<< goodUrl :%d " % (len(data.get('badUrl')),len(data.get('goodUrl')))
    file.close()
    return True

def recurse(urlList,path,deepth=-1):
    if not urlList :
        return None
    if deepth>0:
        deepth -= 1
    elif deepth == 0:
        return None

    for url in urlList:
        content = getHtml(url)
        urlList = getUrl(content)
        tmpUrlList = filter(urlList)
        print "flash disk starting.... >>>  file : "+path
        flashFile({'goodUrl':urlSpidered.keys(),'badUrl':badUrl.keys()},path)
        print "flash disk over !  file : "+path
        countTimes.countTime()
        if tmpUrlList :
            tmpUrlList = sureDomain(tmpUrlList,domain)
            recurse(tmpUrlList,path,deepth)
    print "*"*66
    print json.dumps(urlSpidered.keys())

if __name__ == '__main__':

    print "+"*88
    print "spider start working  "
    countTimes.printCurrentTime()
    director = '../data'
    if not os.path.exists(director):
        os.makedirs(director)
    path = director+'/url.json'
    recurse([domain],path,3)
    print "+"*88
    print "spider worked over !! "
    countTimes.countTime()
    countTimes.printCurrentTime()



