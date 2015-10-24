#coding:utf8
__author__ = 'flybird1971'

import time

start  = time.time()

def countTime():
    end = time.time()
    times = int(end - start)
    mins  = times%3600
    hours = times/3600
    seconds = mins%60
    mins = (int)(mins/60)
    print "*"*120
    print " spend  %d:%d:%d " % (hours,mins,seconds)
    print "*"*120

def printCurrentTime():
    print time.strftime("%Y-%m-%d %H:%M:%S")

