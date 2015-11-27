'''
pyclbr 模块
pyclbr 模块包含一个基本的 Python 类解析器

'''

# 使用 pyclbr 模块
# readmodule 函数:解析给定模块, 返回一个模块所有顶层类组成的列表.
import pyclbr

print(dir(pyclbr))
mod = pyclbr.readmodule('cgi')

for k, v in mod.items():
	print(k, v)

'''
Message <pyclbr.Class object at 0x02D37E90>
Mapping <pyclbr.Class object at 0x02D21FD0>
MiniFieldStorage <pyclbr.Class object at 0x02D37FD0>
FieldStorage <pyclbr.Class object at 0x02DDC470>
[Finished in 1.2s]
'''


print('-------------------------------------------------')



# 使用 pyclbr 模块读取类和函数
# readmodule_ex , 它还会读取全局函数.
import pyclbr

mod = pyclbr.readmodule_ex('cgi')

for k, v in mod.items():
	print(k, v)

'''
parse_qsl <pyclbr.Function object at 0x02C88410>
valid_boundary <pyclbr.Function object at 0x02C88630>
nolog <pyclbr.Function object at 0x02C88390>
parse_header <pyclbr.Function object at 0x02C88470>
print_environ_usage <pyclbr.Function object at 0x02C88610>
closelog <pyclbr.Function object at 0x02C88370>
_parseparam <pyclbr.Function object at 0x02C88450>
escape <pyclbr.Function object at 0x02C88690>
print_exception <pyclbr.Function object at 0x02C88590>
test <pyclbr.Function object at 0x02C88570>
MiniFieldStorage <pyclbr.Class object at 0x02BE7FF0>
Mapping <pyclbr.Class object at 0x02BD1F50>
dolog <pyclbr.Function object at 0x02C7EE70>
parse_qs <pyclbr.Function object at 0x02C883F0>
print_arguments <pyclbr.Function object at 0x02C885F0>
print_directory <pyclbr.Function object at 0x02C885D0>
parse <pyclbr.Function object at 0x02C883D0>
warn <pyclbr.Function object at 0x02C7E830>
print_form <pyclbr.Function object at 0x02C885B0>
FieldStorage <pyclbr.Class object at 0x02C88490>
initlog <pyclbr.Function object at 0x02C7E970>
Message <pyclbr.Class object at 0x02BE7EB0>
parse_multipart <pyclbr.Function object at 0x02C88430>
print_environ <pyclbr.Function object at 0x02C88530>
[Finished in 1.2s]
'''


print('-------------------------------------------------')


# 使用 pyclbr 模块
import pyclbr
import operator
mod = pyclbr.readmodule('cgi')

def dump(c):
	# print class header
	s = 'class' + c.name
	if c.super:
		s = s + '(' + ','.join(map(lambda v: v.name, c.super)) + ')'
		print(s + ':')
	# print method names, sorted by line number
	methods = list(c.methods.items())
	methods.sort()
	for method, lineno in methods:
		print('  def   ' + method)
	print()

for k, v in mod.items():
	dump(v)
'''
[('__repr__', 357), ('__init__', 351)] ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
  def   __init__
  def   __repr__

classMapping(Sized,Iterable,Container):
[('__getitem__', 394), ('get', 397), ('__eq__', 424), ('__contains__', 404), ('values', 420), ('items', 416), ('keys', 412), ('__ne__', 429)] ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
  def   __contains__
  def   __eq__
  def   __getitem__
  def   __ne__
  def   get
  def   items
  def   keys
  def   values

[('__str__', 133), ('add_header', 484), ('set_boundary', 801), ('_get_params_preserve', 593), ('get_boundary', 788), ('replace_header', 514), ('get_unixfrom', 164), ('get_content_maintype', 557), ('get_params', 614), ('keys', 399), ('is_multipart', 154), ('get_content_charset', 847), ('get', 431), ('__init__', 121), ('set_charset', 292), ('attach', 170), ('set_payload', 272), ('__len__', 347), ('get_filename', 772), ('get_charset', 339), ('get_content_type', 533), ('del_param', 718), ('get_charsets', 877), ('get_all', 466), ('set_type', 740), ('__contains__', 392), ('set_param', 670), ('get_payload', 182), ('get_content_subtype', 566), ('raw_items', 455), ('get_param', 636), ('as_string', 139), ('__getitem__', 351), ('set_default_type', 584), ('__delitem__', 380), ('set_unixfrom', 161), ('__iter__', 395), ('values', 409), ('get_default_type', 575), ('set_raw', 448), ('items', 420), ('__setitem__', 362)] ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
  def   __contains__
  def   __delitem__
  def   __getitem__
  def   __init__
  def   __iter__
  def   __len__
  def   __setitem__
  def   __str__
  def   _get_params_preserve
  def   add_header
  def   as_string
  def   attach
  def   del_param
  def   get
  def   get_all
  def   get_boundary
  def   get_charset
  def   get_charsets
  def   get_content_charset
  def   get_content_maintype
  def   get_content_subtype
  def   get_content_type
  def   get_default_type
  def   get_filename
  def   get_param
  def   get_params
  def   get_payload
  def   get_unixfrom
  def   is_multipart
  def   items
  def   keys
  def   raw_items
  def   replace_header
  def   set_boundary
  def   set_charset
  def   set_default_type
  def   set_param
  def   set_payload
  def   set_raw
  def   set_type
  def   set_unixfrom
  def   values

[('__repr__', 563), ('make_file', 851), ('read_urlencoded', 652), ('read_lines_to_outerboundary', 780), ('keys', 631), ('read_lines', 744), ('skip_lines', 829), ('read_binary', 727), ('getfirst', 609), ('read_lines_to_eof', 770), ('getvalue', 598), ('__len__', 643), ('__bool__', 647), ('__write', 755), ('__contains__', 637), ('__getitem__', 584), ('read_multi', 671), ('__iter__', 568), ('__init__', 405), ('read_single', 716), ('__getattr__', 571), ('getlist', 620)] ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
  def   __bool__
  def   __contains__
  def   __getattr__
  def   __getitem__
  def   __init__
  def   __iter__
  def   __len__
  def   __repr__
  def   __write
  def   getfirst
  def   getlist
  def   getvalue
  def   keys
  def   make_file
  def   read_binary
  def   read_lines
  def   read_lines_to_eof
  def   read_lines_to_outerboundary
  def   read_multi
  def   read_single
  def   read_urlencoded
  def   skip_lines

[Finished in 1.2s]
'''




