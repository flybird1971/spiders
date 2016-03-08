#!/usr/bin/env python
#coding:utf8

from socket import *

ADDR = ('127.0.0.1',8534)
Buffer = 1024

client = socket(AF_INET,SOCK_STREAM)
client.connect(ADDR)
print "...connect "
while True:
    data = raw_input('>')
    if not data:
        continue
    if data == 'q':
        break
    client.send(data)
    res = client.recv(Buffer)
    print res
client.close()
print "...connect lose"

