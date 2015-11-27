'''
sunaudio 模块

sunaudio 模块用于识别 Sun AU 音频文件, 并提取其基本信息. 
sunau 模块为 Sun AU 文件提供了更完成的支持. 
'''
import sunaudio

file = "samples/sample.au"
print(sunaudio.gethdr(open(file, "rb")))