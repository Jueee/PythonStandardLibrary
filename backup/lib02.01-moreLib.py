'''
更多标准模块

本章叙述了许多在 Python 程序中广泛使用的模块. 


2.1.1. 文件与流
fileinput 模块可以让你更简单地向不同的文件写入内容. 
该模块提供了一个简单的封装类, 一个简单的 for-in 语句就可以循环得到一个或多个文本文件的内容.

StringIO 模块 (以及 cStringIO 模块, 作为一个的变种) 实现了一个工作在内存的文件对象. 
你可以在很多地方用 StringIO 对象替换普通的文件对象.


2.1.2. 类型封装
UserDict , UserList , 以及 UserString 是对应内建类型的顶层简单封装. 
和内建类型不同的是, 这些封装是可以被继承的. 
这在你需要一个和内建类型行为相似但由额外新方法的类的时候很有用.


2.1.3. 随机数字
random 模块提供了一些不同的随机数字生成器. 

whrandom 模块与此相似, 但允许你创建多个生成器对象.
[!Feather 注: whrandom 在版本 2.1 时声明不支持. 请使用 random 替代.]


2.1.4. 加密算法
md5 和 sha 模块用于计算密写的信息标记( cryptographically strongmessage signatures , 所谓的 "message digests", 信息摘要).

crypt 模块实现了 DES 样式的单向加密. 该模块只在 Unix 系统下可用.

rotor 模块提供了简单的双向加密. 版本 2.4 以后的朋友可以不用忙活了.


'''