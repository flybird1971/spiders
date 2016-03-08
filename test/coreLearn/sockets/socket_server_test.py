#!/usr/bin/env python
#coding:utf8

from socket import *
from time import ctime

host = ''
port = 8534
addr = (host,port)
Buffer = 1024

def tcpServer_s(addr,Buffer):
    tcpServer = socket(AF_INET,SOCK_STREAM)
    tcpServer.bind(addr)
    tcpServer.listen(3)
    # tcpServer.setblocking(False)
    # tcpServer.setdefaulttimeout(1)

    while True:
        print "wait to connection .... "
        cliSocket,cliAddr = tcpServer.accept()
        # cliSocket.setdefaulttimeout(3)
        print "connect from %s:%s " % cliAddr
        while True:
            data = cliSocket.recv(Buffer)
            if not data:
                break
            cliSocket.send("[%s] %s" % (ctime(),data))
            print "connect from %s:%s ;message : %s" % (cliAddr[0],cliAddr[1],data)
        cliSocket.close()
    tcpServer.close()


def udpServer_s(addr,Buffer):
    udpServer = socket(AF_INET,SOCK_DGRAM)
    udpServer.bind(addr)
    print "udp message ... "
    while True:
        data,addr = udpServer.recvfrom(Buffer)
        if not data:break
        print "udp message from %s:%s; message: %s" % (addr[0],addr[1],data)
        udpServer.sendto("[%s] %s" % (ctime(),data),addr)
        
    udpServer.close()

# udpServer_s(addr,Buffer)
# tcpServer_s(addr,Buffer)

from SocketServer import (TCPServer as TCP,StreamRequestHandler as SRH)

class MyRequestHandler(SRH):
    def handle(self):
        print "...connected from :",self.client_address
        self.wfile.write('[%s] %s' % (ctime(),self.rfile.readline()))

# tcpServer = TCP(addr,MyRequestHandler)
# print "waiting for connection ..."
# tcpServer.serve_forever()

from twisted.internet import protocol, reactor, endpoints
class TSServeProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print "...connected from:",clnt

    def dataReceived(self,data):
        print "message from %s: messag:%s " % (self.clnt,data)
        self.transport.write('[%s] %s' % (ctime(),data))

factory = protocol.Factory()
factory.protocol = TSServeProtocol
print "waiting for connection..."
reactor.listenTCP(port,factory)
reactor.run()

