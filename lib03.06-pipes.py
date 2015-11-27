'''
pipes 模块

(只用于 Unix) pipes 模块提供了 "转换管道 (conversion pipelines)" 的支持. 
可以创建包含许多外部工具调用的管道来处理多个文件.
'''

import pipes

t = pipes.Template()
print(t,type(t))

# create a pipeline
# 这里 " - " 代表从标准输入读入内容
t.append("sort", "--")
t.append("uniq", "--")

# filter some text
# 这里空字符串代表标准输出
t.copy("samples/sample.txt", "")


'''
Alan Jones (sensible party)
Kevin Phillips-Bong (slightly silly)
Tarquin
Fin-tim-lin-bin-whin-bim-lin-bus-stop-F'tang-F'tang-Olé-Biscuitbarrel
'''