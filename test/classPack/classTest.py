#coding:utf8

__author__ = 'flybird1971'

#对象练习

class Demo:
    desc = 'this is demo class '

    def show(self):
        print self.desc

class SubOne(Demo):
	pass

class SubTwo(Demo):
	pass

		
print Demo.desc,SubOne.desc,SubTwo.desc;

SubOne.desc = 'this is son one demo '
print Demo.desc,SubOne.desc,SubTwo.desc;

Demo.desc = ' modifty base class demoe description '
print Demo.desc,SubOne.desc,SubTwo.desc;

SubTwo.desc = ' modifty son two description'
print Demo.desc,SubOne.desc,SubTwo.desc;

print "*"*80
li = [lambda x : x**x for x in range(5)]
print li

while True:
	inputStr = raw_input("请输入数字或'q'退出：")
	if inputStr=='q':break;
	print "你输入字符串：%s " % (inputStr)

demo = Demo()
demo.show()