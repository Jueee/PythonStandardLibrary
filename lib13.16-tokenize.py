'''
tokenize 模块

tokenize 模块将一段 Python 源文件分割成不同的 token . 
可以在代码高亮工具中使用它.
'''
import tokenize

file = open('lib13.16-tokenize.py')

def handle_token(type, token, srow, scol, erow, ecol, line):
	print('%d,%d-%d,%d:\t%s\t%s' % (srow,scol,erow,tokenize.tok_name[type],token))

tokenize.tokenize(file.readline, handle_token)