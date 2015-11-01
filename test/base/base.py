#coding:utf8
__author__ = 'flybird1971'

name = raw_input("please input name : ")
age = raw_input("please input age : ")
sex = input("please input sex : ")

if age > 40 :
    print "age : %s" % (age)

for t in xrange(12):
    sum = t
    print t

print "*"*23
print sum


print """
      show you enter sex :
          name : %s
          age  : %d
          sex  : %d
"""  % (name,int(age),sex)