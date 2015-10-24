#coding:utf8

import copy 
__author__ = 'flybird1971'

list = [1,2,3,['e','c','e']]

#python编译时，会建立常量池，int string常量存储在常量池中
#其他地方直接引用常量池地址，不再新开辟内存空间

listA = list

#浅拷贝
listB = copy.copy(list)

#深拷贝
listC = copy.deepcopy(list)

print "*"*55
print list
print listA
print listB
print listC

list.append('e')
print "*"*55
print list
print listA
print listB
print listC

print "*"*55
list[3].append('c')
print list
print listA
print listB
print listC
