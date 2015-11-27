'''
shlex 模块

shlex 模块为基于 Unix shell 语法的语言提供了一个简单的 lexer (也就是 tokenizer).
'''
import shlex

lexer = shlex.shlex(open('samples/sample.netrc', 'r'))

while 1:
	token = lexer.get_token()
	if not token:
		break
	print(token)
