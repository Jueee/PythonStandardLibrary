'''
ucnhash 模块

ucnhash 模块为一些 Unicode 字符代码提供了特定的命名.
你可以直接使用 \N{} 转义符将 Unicode 字符名称映射到字符代码上.

'''
'''
# Python imports this module automatically, when it sees
# the first \N{} escape
# import ucnhash
'''
print(repr(u"\N{FROWN}"))
print(repr(u"\N{SMILE}"))
print(repr(u"\N{SKULL AND CROSSBONES}"))