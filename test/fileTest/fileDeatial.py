#coding:utf8
'''
autho : flybird1971@gmail.com
since : 2015-10-31 15:23:43
'''



f = open('../data/ts.json','r+')
print f.read().decode('utf8')
f.seek(0,2)
f.write("中华人民共和国")
print f.tell()
print "*"*88
f.seek(0,2)
result = []
for i in xrange(10):
    result.append(str(i)+"\n")
f.writelines(result)
f.close()

import time
def tail():
    print "-"*77
    prePos = 0
    while True:
        f = open('../data/tmp.data')
        f.seek(prePos) #指针移到上次开始追加位置
        print f.read()
        prePos = f.tell()
        print "."*32
        f.seek(0,2)  #指针移到文件尾
        f.close()
        for index in xrange(10):
            time.sleep(1)
            print (9-index)
#tail()


print __file__
print __doc__
print __name__
