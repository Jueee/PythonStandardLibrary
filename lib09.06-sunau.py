'''
sunau 模块

sunau 模块用于读写 Sun AU 音频文件. 
'''
import sunau

w = sunau.open('samples/sample.au', 'r')

if w.getnchannels() == 1:
	print("mono,",)
else:
	print("stereo,",)
	print(w.getsampwidth()*8, "bits,",)
	print(w.getframerate(), "Hz sampling rate")






