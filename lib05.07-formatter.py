'''
formatter 模块

formatter 模块提供了一些可用于 htmllib 的格式类( formatter classes ).

这些类有两种,  formatter 和  writer . 
formatter 将 HTML 解析器的标签和数据流转换为适合输出设备的事件流( event stream ), 而 writer 将事件流输出到设备上.
'''
# 使用 formatter 模块将 HTML 转换为事件流
import formatter

w = formatter.AbstractWriter()
f = formatter.AbstractFormatter(w)

