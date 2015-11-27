'''
webbrowser 模块

(2.0 中新增) webbrowser 模块提供了一个到系统标准 web 浏览器的接口. 

它提供了一个 open 函数, 接受文件名或 URL 作为参数, 然后在浏览器中打开它.

如果你又一次调用 open 函数, 那么它会尝试在相同的窗口打开新页面.
'''
import webbrowser
import time

webbrowser.open('http://www.baidu.com')

time.sleep(5)
webbrowser.open('http://www.zhihu.com/#welcome')






