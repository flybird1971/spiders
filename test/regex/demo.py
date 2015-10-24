#coding:utf8
import spiderTool as spider
import countTimes
import  os
__author__ = 'flybird1971'

#抓取网站域名
domain = 'http://www.guonainai.com'


print "+"*88
print "spider start working  "
countTimes.printCurrentTime()
director = '../data'
if not os.path.exists(director):
    os.makedirs(director)
path = director+'/url.json'
spider.recurse([domain],path)
print "+"*88
print "spider worked over !! "
countTimes.countTime()
countTimes.printCurrentTime()
