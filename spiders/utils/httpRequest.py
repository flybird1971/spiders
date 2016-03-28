#!/usr/bin/env python
# coding:utf-8
"""
pip install rsa
"""

import urllib
import urllib2
import rsa

PUBLIC_KEY = '../keyPath/rsa_public_key.pem'


class HttpRequest(object):

    def __init__(self, url='', requestType='post'):
        self.url = url
        self.type = requestType

    def setUrl(self, url):
        self.url = url
        return self

    def getUrl(self):
        return self.url

    def setRequestType(self, requestType):
        self.requestType = requestType
        return self

    def getRequestType(self):
        return self.requestType

    def setBody(self, body):
        self.body = body
        return self

    def getBody(self):
        return self.body

    def post(self):
        if not self.url:
            raise Exception('url must not emptye')

        self.setRequestType('post')
        return self.send()

    def get(self):
        if not self.url:
            raise Exception('url must not emptye')

        self.setRequestType('get')
        self.url = self.url + '?' + urllib.urlencode(self.body)
        return self.send()

    def send(self):
        try:
            if self.requestType == 'post':
                self.body = urllib.urlencode(self.body)
                req = urllib2.Request(url=self.url, data=self.body)
            else:
                req = urllib2.Request(self.url)

            response = urllib2.urlopen(req)
            response = response.read()
            return response
        except (Exception, HTTPError), e:
            raise
        finally:
            pass

    def encrypt(self, encryptFields):

        publicKey = rsa.PublicKey.load_pkcs1_openssl_pem(b"""-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCU9h4YazGDzLggcfiWqVftim3A
nWLMPACImzsG7ebMw/tpejJ3C2WBVtJXJb+kAKeKX5R3FGltqCbIW1B7Id3v2sLb
p//MUEeY4RpnlVaAcH3LJVYkqYy0wZcddn5Y8VsAXeMqjsvyPvgNMCoNke4czqso
JZ8HrqvnB37G/vRmdQIDAQAB
-----END PUBLIC KEY-----""")
        for i, key in enumerate(encryptFields):
            self.body[key] = rsa.encrypt(self.body[key], publicKey)
        # print self.body
        return self

if __name__ == '__main__':
    http = HttpRequest()
    url = 'http://www.babel.com/api/get-spider-rules/get'
    body = {'action': 'get', 'version': '1.1'}
    encryptFields = ['action', 'version']
    print http.setUrl(url).setBody(body).encrypt(encryptFields).post()
