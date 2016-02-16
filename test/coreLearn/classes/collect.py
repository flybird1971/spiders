#! /usr/bin/env python
# -*- coding=utf-8 -*-
# @Author pythontab.com

import urllib2
import socket
import re
import urlparse

from test import ParseHeader


def get_url_content(url):
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",
                 "Referer": 'http://www.baidu.com'}
    req = urllib2.Request(url, headers=i_headers)

    return urllib2.urlopen(req).read()


def __fromat(data, prefix):
    regex = re.compile('<(.*)(src|href)(=[\'"])[^h](.*[\'"])+?', re.I | re.M)
    res = regex.sub(r'<\1 \2 \3' + prefix + '/\4', data)
    return res


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8080))
    sock.listen(5)
    while True:
        connection, address = sock.accept()
        try:
            connection.settimeout(10)
            buf = connection.recv(1024)

            pheader = ParseHeader(buf)
            pheader.parse()
            getInfo = pheader.getGet()
            if not getInfo.get('url', None):
                raise ValueError, 'you must enter url'

            url = getInfo.get('url')
            urlLi = urlparse.urlparse(url)
            prefix = urlLi.scheme + '://' + urlLi.netloc

            respond = get_url_content(url)
            respond = __fromat(respond, prefix)
            connection.send(respond)

        except (Exception, ValueError, socket.timeout):
            print 'has error'
        connection.close()

server()
# print "-" * 66
# print get_url_content('https://segmentfault.com/q/1010000000126349')
# print "-" * 66

# url = "https://www.baidu.com"
# req_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#               'Accept': 'text/html;q=0.9,*/*;q=0.8',
#               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#               'Accept-Encoding': 'gzip',
#               'Connection': 'close',
# 'Referer': None  # 注意如果依然不能抓取的话，这里可以设置抓取网站的host
#               }
# req_timeout = 10
# req = urllib2.Request(url, None, req_header)
# resp = urllib2.urlopen(req, None, req_timeout)
# html = resp.read()
# print "-" * 66
# print html
# print "-" * 66
