'''
pprint 模块

pprint 模块( pretty printer )用于打印 Python 数据结构. 
当你在命令行下打印特定数据结构时你会发现它很有用(输出格式比较整齐, 便于阅读).
'''
import pprint

data = (
"this is a string", [1, 2, 3, 4], ("more tuples",
1.0, 2.3, 4.5), "this is yet another string"
)
pprint.pprint(data)
