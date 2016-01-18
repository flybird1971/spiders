# /usr/bin/env python
# encoding:utf8

import urllib2
import time

hosts = ["http://yahoo.com", "http://www.baidu.com", "http://www.sina.cn",
         "http://www.ibm.com", "http://www.apple.com"]

start = time.time()
# grabs urls of hosts and prints first 1024 bytes of page
for host in hosts:
    url = urllib2.urlopen(host)
    print url.read(1024)

print "Elapsed Time: %s" % (time.time() - start)
