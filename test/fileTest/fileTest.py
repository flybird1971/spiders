#coding:utf8
import time
__author__ = 'flybird1971'


#fileHandle = open('../data/t.json','a+')
#content = fileHandle.read()
#fileHandle.write('content\n')
#fileHandle.close()



#fileHandle.readline()
#fileHandle.readlines()

#fileHandle.next()

#文件指针移动
#offset 偏移量，option模式选择
#offset >0  右偏移  <0 左偏移  =0不偏移
#option  =0  文件头，=1 文件中  =2 文件尾
print "*"*39
f = open('../data/ts.json','w+')
offset = 0
option = 2
f.seek(offset,option)
list = f.readlines()
str = "\n\n aaaaaaaaaaaaaaaaaaaaaa\n\n"
f.seek(0,2)
f.write(str)
l = ['aa','bbb','ccc']
f.writelines(l)

f.seek(0,0)
print f.read()
f.close()

print "*"*313
f = open('../data/t.json','r+')
cont = f.read()
print cont
print "-"*88
f.truncate(0) #截断文件，
f.seek(0,0)
f.write('cont')
f.close()


#################################################
#####  os
#################################################
import os

oldPath = os.getcwd()
print oldPath
#创建文件夹
path = '../data/test'
if not os.path.exists(path):
    os.mkdir(path)

#递归创建文件夹
pathRecurise = '../data/test/test/test'
if not os.path.exists(pathRecurise):
    os.makedirs(pathRecurise)

#切换目录
os.chdir('../../')

#show当前目录
currentPath = os.getcwd()
os.chdir(oldPath)
#list目录
print os.listdir('.')

#删除空文件夹
#os.rmdir(pathRecurise)

#递归删除文件夹
#os.removedirs(path)

print "+"*44
#递归遍历文件夹，返回列表
def showDirect(direct):
    result = []
    if not os.path.isdir(direct):
        return result
    dirList = os.listdir(direct)
    if not dirList:
        return result
    for tmp in dirList:
        tmpAbsPath = os.path.join(direct,tmp)
        if os.path.isfile(tmpAbsPath):
            absPath = os.path.abspath(tmpAbsPath)
            result.append(absPath)
        elif os.path.isdir(tmpAbsPath):
            result.extend( showDirect(tmpAbsPath))
        else:
            pass
    return result

res = showDirect('../../../css')
print "+"*44
print "total %d files " % (len(res))
f = open('../data/t.json','r+')
f.truncate(0)
f.seek(0,0)
f.writelines(res)
f.close()
for t in res:
    print t



