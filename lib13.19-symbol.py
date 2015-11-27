'''
symbol 模块

symbol 模块包含 Python 语法中的非终止符号. 

可能只有你涉及 parser 模块的时候用到它. 
'''

import symbol

print(dir(symbol))
print('print', symbol.import_stmt)
print('return', symbol.return_stmt)