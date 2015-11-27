'''
binhex 模块

binhex 模块用于到 Macintosh BinHex 格式的相互转化.
'''
# 使用 binhex 模块
import binhex
import sys

infile = 'samples/sample.jpg'
print(type(sys.stdout), sys.stdout)
print(type(infile), infile)
binhex.binhex(infile, sys.stdout)