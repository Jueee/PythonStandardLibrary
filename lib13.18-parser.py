'''
parser 模块

(可选) parser 模块提供了一个到 Python 内建语法分析器和编译器的接口.
'''
import parser
import symbol, token

def dump_and_modify(node):
	name = symbol.sym_name.get(node[0])
	if name is None:
		name = token.tok_name.get(node[0])
	print(name, '', end = '')
	for i in range(1, len(node)):
		item = node[i]
		if type(item) is type([]):
			dump_and_modify(item)
		else:
			print(repr(item))
			if name == 'NUMBER':
				node[i] = repr(int(item) + 1)

ast = parser.expr('1 + 3')
list = ast.tolist()
dump_and_modify(list)

ast = parser.sequence2st(list)
print(eval(parser.compilest(ast)))

'''
eval_input testlist test or_test and_test not_test comparison expr xor_expr and_expr shift_expr arith_expr term factor power atom NUMBER '1'
PLUS '+'
term factor power atom NUMBER '3'
NEWLINE ''
ENDMARKER ''
6
[Finished in 0.2s]
'''












