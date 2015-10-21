#coding:utf8
__author__ = 'flybird1971'

#字符比较函数
def compStr(str='d',cpStr='sdd'):
    if str == cpStr :
        print(str+" == "+cpStr)
    else:
        print(str+" != "+cpStr)


s1 = raw_input("input")
s2 = raw_input("sssss")
compStr(s1,s2)
compStr()

str = 'ss'
while str != 'q':
    str = raw_input("enter q to exit : ")
    if str=='q':
        break
    str2 = raw_input("please input second string : ")
    compStr(str,str2)
print("*"*32)

print(str)

print "-"*42
dic = {"age":"li","name":30}
list = ["li",30]
def showInfos(name,age):
    print (name,age)

#取字典 值传参
showInfos(**dic)
#取字典 key传参
showInfos(*dic)

print "*"*44
#取列表值 传参
showInfos(*list)

print "*"*44
#接受多于参数，无映射关系存入元祖中 有映射关系存入字典
def show(x,*ohterArgs,**dic):
    print x
    print ohterArgs
    print dic

show(1)
print "*"*33
show (1,2,3,4,5,6)
print "*"*33
show(1,1,2,xs=1,y=2)