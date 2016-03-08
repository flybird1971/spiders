#!/usr/bin/env python
#coding:utf8

from socket import *
from time import ctime
import os
import re

class SocketSeverCommand(object):

    def __init__(self,host,port,buffer=1024):
        self.host = host
        self.port = port
        self.buffer = buffer

    def getDate(self,*argsTuple,**argsDict):
        return "[%s]" % ctime()

    def getOS(self,*argsTuple,**argsDict):
        return os.name
        
    def showDirect(self,dirct='',*argsTuple,**argsDict):
        if not dirct:
            dirct = os.curdir
        return os.listdir(dirct)
        

    def parseCommand(self,command,*argsTuple,**argsDict):
        commandDict = {
            'date' : self.getDate,
            'os' : self.getOS,
            'ls' : self.showDirect
        }

        commandFunc = commandDict.get(command,None)
        if not commandFunc:
            return "no command : %s" % command

        return commandFunc(*argsTuple,**argsDict)


    def start(self):
        server = socket(AF_INET,SOCK_STREAM)
        server.bind((self.host,self.port))
        server.listen(5)
        print "waiting for connect....."
        while True:
            client,addr = server.accept()
            print "...connect from %s:%s" % addr
            while True:
                data = client.recv(self.buffer)
                if not data:
                    break
                data = re.sub(r'\s+',' ',data)
                dataList = data.split(' ')
                print "recive data :%s" % dataList
                if not dataList:
                    continue
                command = dataList[0]
                argsTuple = tuple(dataList[1:])
                res = self.parseCommand(command,*argsTuple)
                client.send("%s" % res)
            client.close()
            print "...connected lose %s:%s" % addr
        server.close()

s = SocketSeverCommand('127.0.0.1',8534)
s.start()