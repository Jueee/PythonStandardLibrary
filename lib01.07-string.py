'''
string 模块

string 模块提供了一些用于处理字符串类型的函数
'''

# 使用 string 模块
import string

text = "Monty Python's Flying Circus"
print("upper", "=>", str.upper(text))
print("lower", "=>", str.lower(text))
print("split", "=>", str.split(text))
print("join", "=>", '+'.join(str.split(text)))
print("replace", "=>", str.replace(text, "Python", "Java"))
print("find", "=>", str.find(text, "Python"), str.find(text,"Java"))
print("count", "=>", str.count(text, "n"))
'''
upper => MONTY PYTHON'S FLYING CIRCUS
lower => monty python's flying circus
split => ['Monty', "Python's", 'Flying', 'Circus']
join => Monty+Python's+Flying+Circus
replace => Monty Java's Flying Circus
find => 6 -1
count => 3
'''



# 使用字符串方法替代 string 模块函数
text = "Monty Python's Flying Circus"
print("upper", "=>", text.upper())
print("lower", "=>", text.lower())
print("split", "=>", text.split())
print("join", "=>", "+".join(text.split()))
print("replace", "=>", text.replace("Python", "Perl"))
print("find", "=>", text.find("Python"), text.find("Perl"))
print("count", "=>", text.count("n"))
'''
upper => MONTY PYTHON'S FLYING CIRCUS
lower => monty python's flying circus
split => ['Monty', "Python's", 'Flying', 'Circus']
join => Monty+Python's+Flying+Circus
replace => Monty Perl's Flying Circus
find => 6 -1
count => 3
'''









juestr = "  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  "
sub = "s"

print(juestr.count(sub)			,'返回：sub在juestr中出现的次数                                                            ')
print(juestr.find(sub)				,'返回：从左开始，查找sub在juestr中第一次出现的位置。如果juestr中不包含sub，返回 -1           ')
print(juestr.index(sub)			,'返回：从左开始，查找sub在juestr中第一次出现的位置。如果juestr中不包含sub，举出错误          ')
print(juestr.rfind(sub)			,'返回：从右开始，查找sub在juestr中第一次出现的位置。如果juestr中不包含sub，返回 -1           ')
print(juestr.rindex(sub)			,'返回：从右开始，查找sub在juestr中第一次出现的位置。如果juestr中不包含sub，举出错误          ')
'''
3 返回：sub在juestr中出现的次数                                                            
16 返回：从左开始，查找sub在juestr中第一次出现的位置。如果juestr中不包含sub，返回 -1           
16 返回：从左开始，查找sub在juestr中第一次出现的位置。如果juestr中不包含sub，举出错误          
29 返回：从右开始，查找sub在juestr中第一次出现的位置。如果juestr中不包含sub，返回 -1           
29 返回：从右开始，查找sub在juestr中第一次出现的位置。如果juestr中不包含sub，举出错误 
'''

print(juestr.isalnum()				,'返回：True， 如果所有的字符都是字母或数字                                             ')
print(juestr.isalpha()				,'返回：True，如果所有的字符都是字母                                                    ')
print(juestr.isdigit()				,'返回：True，如果所有的字符都是数字                                                    ')
print(juestr.istitle()				,'返回：True，如果所有的词的首字母都是大写                                              ')
print(juestr.isspace()				,'返回：True，如果所有的字符都是空格                                                    ')
print(juestr.islower()				,'返回：True，如果所有的字符都是小写字母                                                ')
print(juestr.isupper()				,'返回：True，如果所有的字符都是大写字母                                                ')
'''
False 返回：True， 如果所有的字符都是字母或数字                                             
False 返回：True，如果所有的字符都是字母                                                    
False 返回：True，如果所有的字符都是数字                                                    
False 返回：True，如果所有的词的首字母都是大写                                              
False 返回：True，如果所有的字符都是空格                                                    
False 返回：True，如果所有的字符都是小写字母                                                
False 返回：True，如果所有的字符都是大写字母
'''

print(juestr.join(juestr)				,'返回：将s中的元素，以juestr为分割符，合并成为一个字符串。                                ')
print(juestr.strip()				,'返回：去掉字符串开头和结尾的空格。也可以提供参数sub，去掉位于字符串开头和结尾的sub .  ')	#当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')
print(juestr.replace(sub,"new_sub")	,'返回：用一个新的字符串new_sub替换juestr中的sub                                           ')
print(juestr.capitalize()			,'返回：将juestr第一个字母大写                                                             ')
print(juestr.lower()				,'返回：将juestr全部字母改为小写                                                           ')
print(juestr.upper()				,'返回：将juestr全部字母改为大写                                                           ')
print(juestr.swapcase()			,'返回：将juestr大写字母改为小写，小写改为大写                                             ')
print(juestr.title()				,'返回：将juestr的每个词(以空格分隔)的首字母大写                                           ')
print(juestr.center(100)			,'返回：长度为width的字符串，将原字符串放入该字符串中心，其它空余位置为空格。           ')
print(juestr.ljust(100)			,'返回：长度为width的字符串，将原字符串左对齐放入该字符串，其它空余位置为空格。         ')
print(juestr.rjust(100)			,'返回：长度为width的字符串，将原字符串右对齐放入该字符串，其它空余位置为空格。         ')
'''
   qwwAFAFGWdh, asIYGDask, fhaskdihfcg     qwwAFAFGWdh, asIYGDask, fhaskdihfcg  q  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  w  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  w  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  A  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  F  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  A  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  F  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  G  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  W  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  d  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  h  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  ,  qwwAFAFGWdh, asIYGDask, fhaskdihfcg     qwwAFAFGWdh, asIYGDask, fhaskdihfcg  a  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  s  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  I  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  Y  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  G  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  D  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  a  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  s  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  k  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  ,  qwwAFAFGWdh, asIYGDask, fhaskdihfcg     qwwAFAFGWdh, asIYGDask, fhaskdihfcg  f  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  h  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  a  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  s  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  k  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  d  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  i  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  h  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  f  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  c  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  g  qwwAFAFGWdh, asIYGDask, fhaskdihfcg     qwwAFAFGWdh, asIYGDask, fhaskdihfcg    返回：将s中的元素，以juestr为分割符，合并成为一个字符串。                                
qwwAFAFGWdh, asIYGDask, fhaskdihfcg 返回：去掉字符串开头和结尾的空格。也可以提供参数sub，去掉位于字符串开头和结尾的sub .  
  qwwAFAFGWdh, anew_subIYGDanew_subk, fhanew_subkdihfcg   返回：用一个新的字符串new_sub替换juestr中的sub                                           
  qwwafafgwdh, asiygdask, fhaskdihfcg   返回：将juestr第一个字母大写                                                             
  qwwafafgwdh, asiygdask, fhaskdihfcg   返回：将juestr全部字母改为小写                                                           
  QWWAFAFGWDH, ASIYGDASK, FHASKDIHFCG   返回：将juestr全部字母改为大写                                                           
  QWWafafgwDH, ASiygdASK, FHASKDIHFCG   返回：将juestr大写字母改为小写，小写改为大写                                             
  Qwwafafgwdh, Asiygdask, Fhaskdihfcg   返回：将juestr的每个词(以空格分隔)的首字母大写                                           
                                qwwAFAFGWdh, asIYGDask, fhaskdihfcg                                  返回：长度为width的字符串，将原字符串放入该字符串中心，其它空余位置为空格。           
  qwwAFAFGWdh, asIYGDask, fhaskdihfcg                                                                返回：长度为width的字符串，将原字符串左对齐放入该字符串，其它空余位置为空格。         
                                                               qwwAFAFGWdh, asIYGDask, fhaskdihfcg   返回：长度为width的字符串，将原字符串右对齐放入该字符串，其它空余位置为空格。         
'''


print(juestr.split(','))    		#返回：从左开始，以空格为分割符(separator)，将juestr分割为多个子字符串，总共分割max次。将所得的子字符串放在一个表中返回。可以juestr.split(',')的方式使用逗号或者其它分割符
print(juestr.split(',',0)) 
print(juestr.split(',',1)) 
print(juestr.split(',',2)) 
print(juestr.split(',',-1)) 		#b.split("..",-1)等价于b.split("..") 
print(juestr.rsplit(','))   		#返回：从右开始，以空格为分割符(separator)，将juestr分割为多个子字符串，总共分割max次。将所得的子字符串放在一个表中返回。可以juestr.rsplit(',')的方式使用逗号或者其它分割符
'''
['  qwwAFAFGWdh', ' asIYGDask', ' fhaskdihfcg  ']
['  qwwAFAFGWdh, asIYGDask, fhaskdihfcg  ']
['  qwwAFAFGWdh', ' asIYGDask, fhaskdihfcg  ']
['  qwwAFAFGWdh', ' asIYGDask', ' fhaskdihfcg  ']
['  qwwAFAFGWdh', ' asIYGDask', ' fhaskdihfcg  ']
['  qwwAFAFGWdh', ' asIYGDask', ' fhaskdihfcg  ']
'''