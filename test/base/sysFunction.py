#encoding:utf8

__author__ = 'flybird1971'

list = [1,2,3,4,5,5]
print max(list)
print min(list)

print len(list)

# (10-10%3)/3 10%3
print divmod(10,3)

# 2**3
print pow(2,3)

#3**2 % 4
print pow(3,2,4)

#指定精度返回浮点数
print round(12,1)

print "*"*32
t = 'a'
#检查指定函数是否可用
print callable(round)
print callable(list)

#检测对象类型
print type(1)
print type(callable)
print type(list)
print type(None)

print isinstance(1,int)


print xrange(1,2,4)
print range(1,2,4)

#类型强制转换
print '*'*23
print int(2.3)
print float(2)
print tuple(list)
print long(2)
print complex(2,3)

print "123" + str(122)
print int('123') + 12

#取字符编码
print ord('c')

#返回 编码对应字符
print chr(34)


print hex(122)
print oct(10)

# ++++++++++++++++++++++++++++++++++++++++++++
# 字符串相关内置函数
#help(str)

# ++++++++++++++++++++++++++++++++++++++++++++
# 列表相关内置函数

# 过滤列表
print filter(lambda x : x>5,range(1,39,3))

#对列表每个元素，进行函数处理，
print map(lambda  x,y:x+y,range(1,20),range(21,40))

#递归，处理列表，每次接受两个参数
print reduce(lambda  x,y:x*y,range(1,20))

#打包多个列表为元祖列表，以最小列表个数作为新列表个数
print zip(range(10),range(10,19),range(20,27))




