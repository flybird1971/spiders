#!/usr/bin/env python
#coding:utf8

from socket import *

host = '192.168.1.102'
# host = '127.0.0.1'
port = 8534
addr = (host,port)
Buffer = 1024

def tcpClient_s(addr,Buffer):
    tcpClient = socket(AF_INET,SOCK_STREAM)
    tcpClient.connect(addr)
    while True:
        data = raw_input('>')
        if data=='q':
            break
        tcpClient.send(data)
        res = tcpClient.recv(Buffer)
        print res

    tcpClient.close()

def tcpClient_ss(addr,Buffer):

    while True:
        tcpClient = socket(AF_INET,SOCK_STREAM)
        tcpClient.connect(addr)
        data = raw_input('>')
        if data=='q':
            break
        tcpClient.send("%s\r\n" % data)
        res = tcpClient.recv(Buffer)
        print res.strip()
        tcpClient.close()

def udpClient_s(addr,Buffer):
    udpClient = socket(AF_INET,SOCK_DGRAM)
    while True:
        data = raw_input('>')
        if not data : break
        udpClient.sendto(data,addr)
        res,addr = udpClient.recvfrom(Buffer)
        print "udp message: %s ; %s:%s" % (res,addr[0],addr[1])
    udpClient.close()

#udpClient_s(addr,Buffer)
# tcpClient_ss(addr,Buffer)

from twisted.internet import protocol,reactor

class TCPClnProtocol(protocol.Protocol):

    def sendData(self):
        data = raw_input('>')
        if data == 'q':
            self.transport.loseConnection()
        if data:
            self.transport.write(data)

    def connectionMade(self):
        self.sendData()

    def dataReceived(self,data):
        print data
        self.sendData()

class TCPClnFactory(protocol.ClientFactory):
    protocol = TCPClnProtocol
    clientConnectionLost = clientConnectionFailed = lambda self,connector,reason:reactor.stop()

reactor.connectTCP(host,port,TCPClnFactory())
reactor.run()