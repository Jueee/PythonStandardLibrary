'''
re 模块

re 模块提供了一系列功能强大的正则表达式 (regular expression) 工具
1、检查给定字符串是否与给定的模式匹配 (使用 match 函数)
2、检查给定字符串是否包含这个模式 (使用 search 函数). 

正则表达式是以紧凑(也很神秘)的语法写出的字符串模式.
'''

# 使用 re 模块来匹配字符串
# match 尝试从字符串的起始匹配一个模式
# 如果模式匹配了某些内容 (包括空字符串, 如果模式允许的话) , 它将返回一个匹配对象. 
# 使用它的 group 方法可以找出匹配的内容.
import re

text = 'The Attila the Hun Show.'
# a single character 单个字符
m = re.match('.',text)
if m:
	print(repr('.'),'=>',repr(m.group(0)))
# any string of characters 任何字符串
m = re.match('.*',text)
if m:
	print(repr('.*'),'=>',repr(m.group(0)))
# a string of letters (at least one) 只包含字母的字符串(至少一个)
m = re.match('\w+',text)
if m:
	print(repr('\w+'),'=>',repr(m.group(0)))
# a string of digits 只包含数字的字符串
m = re.match('\d+',text)
if m:
	print(repr('\d+'),'=>',repr(m.group(0)))




# 使用 re 模块抽出匹配的子字符串
# 可以使用圆括号在模式中标记区域. 找到匹配后, group 方法可以抽取这些区域的内容
import re
text = '10/15/99'
m = re.match('(\d{2})/(\d{2})/(\d{2,4})',text)
if m:
	print(m.group(1,2,3))



# 使用 re 模块搜索子字符串
# search 函数会在字符串内查找模式匹配. 
# 它在所有可能的字符位置尝试匹配模式, 从最左边开始, 一旦找到匹配就返回一个匹配对象. 如果没有找到相应的匹配, 就返回  None .
import re
text = 'Example 3: There is 1 date 10/25/95 in here!'
m = re.search('(\d{1,2})/(\d{1,2})/(\d{2,4})',text)
print(m.group(1),m.group(2),m.group(3))

month,day,year = m.group(1,2,3)
print(month,day,year)

date = m.group(0)
print(date)




# 使用 re 模块替换子字符串
import re
text = "you're no fun anymore..."
# 文字替换 (string.replace 速度更快)
print(re.sub('fun','entertaining',text))
print(text.replace('fun','entertaining'))

# 将所有非字母序列转换为一个"-"(dansh,破折号)
print(re.sub('[^\w]+','-',text))

# 将所有单词替换为 BEEP
print(re.sub('\S+','-BEEP-',text))

'''
you're no entertaining anymore...
you're no entertaining anymore...
you-re-no-fun-anymore-
-BEEP- -BEEP- -BEEP- -BEEP-
'''





# 使用 re 模块替换字符串(通过回调函数)
# 也可以通过回调 (callback) 函数使用 sub 来替换指定模式.
import re
import string
text = 'a line of text\\012another line of text\\012etc...'
def octal(match):
	# # 使用对应 ASCII 字符替换八进制代码
	return chr(int(match.group(1),8))
octal_pattern = re.compile(r'\\(\d\d\d)')
print(text)
print(octal_pattern.sub(octal,text))
'''
a line of text\012another line of text\012etc...
a line of text
another line of text
etc...
'''




# 使用 re 模块匹配多个模式中的一个
import re
def combined_pattern(patterns):
	p = re.compile('|'.join(map(lambda x:'('+x+')',patterns)))
	def fixup(v,m=p.match,r=range(0,len(patterns))):
		try:
			regs = m(v).regs
		except AttributeError:
			return None
		else:
			for i in r:
				if regs[i+1] != (-1,-1):
					return i
	return fixup


patterns = [r'\d+',r'abc\d{2,4}',r'p\w+']
p = combined_pattern(patterns)
print(p("129391"))
print(p("abc800"))
print(p("abc1600"))
print(p("python"))
print(p("perl"))
print(p("tcl"))


