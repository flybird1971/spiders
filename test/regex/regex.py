#encoding:utf8
import re as regex
import sys
sys.path.append("../")
__author__ = 'flybird1971'

pattern = r"((\w|\d|.)*[a-z\$])"
str = 'abd$c'
print regex.findall(pattern,str)


#禁止贪恋匹配
#pattern = r".+" 贪恋模式
pattern =r".+?"
print regex.findall(pattern,str)

#正则 编译提速
testRegex = regex.compile(pattern)
testRegexCase = regex.compile(pattern,regex.I)
print testRegex.findall('aaaaaaaaaaa')

print '-'*44
str = 'apple bannar fruit liuxue'
#match     从开头进行匹配，匹配成功返回match对象，否则None
#search    全局匹配，成功返回match对象，否则None
#findall   匹配所以字符串，返回列表，
#finditer  返回匹配迭代器，fiter.next.group()
#sub       正则替换子字符串
#subn      正则替换子字符串，返回元组，（newStr,replaceTimes）
#split     正则切割字符串
matchReg   = regex.compile(r'[ab]')
searchReg  = regex.compile(r'[ab]')
findallReg = regex.compile(r'[ab]')
fiterReg   = regex.compile(r'[ab]')
subReg     = regex.compile(r'[ab]')
subnReg    = regex.compile(r'[ab]')
splitReg = regex.compile(r'\s')

print matchReg.match(str).group()
print searchReg.search(str).group()
print findallReg.findall(str,0)
print fiterReg.finditer(str)
print subnReg.sub('*',str)
print subnReg.subn('+',str,12)
print splitReg.split(str,4)

#match对象
#   group()  返回匹配结果
#   start()  返回匹配开始位置
#   end()    返回匹配结束位置
#   span()   返回一个元组（开始，结束）的位置

print '-'*50
str = 'apple\nAPPLE\n fruit'
#编译标志 flags
#DOTALL,S      使 '.' 匹配包括换行在内的所有字符
#IGNORECASE,I  忽略大小写匹配
#LOCAL,L       做本地化标识(locale-aware) 匹配
#MULTILINE,M   匹配多行，对元组 '^','$' 有影响
#VERBOSE,X     正则规则多行，用此格式化正则， RES verbose状态，组织更清晰易懂
sCharReg = regex.compile(r'apple.',regex.S)
iCharReg = regex.compile(r'A',regex.I)
mCharReg = regex.compile(r'^.+$',regex.M)
patter = r'''t
aaa
aa
'''
print patter
print sCharReg.findall(str)
print iCharReg.findall(str)
print mCharReg.findall(str)


print "-"*55
str = 'www.baidu.com'
#正则分组,正则处理，返回各分组数据
groupReg = regex.compile(r'^(www\.(\w+)\.(cn|org|com|net))$')
print groupReg.match(str).group()
print groupReg.match(str).groups()
print groupReg.findall(str)

