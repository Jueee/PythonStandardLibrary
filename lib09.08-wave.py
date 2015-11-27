'''
wave int)模块

wave 模块用于读写 Microsoft WAV 音频文件
'''
import wave

w = wave.open('samples/sample.wav', 'r')
if w.getnchannels() == 1:
	print('mono')
else:
	print('st')

print(w.getsampwidth() * 8, 'bits')
print(w.getframerate(), 'Hz sampling rate')
'''
mono
8 bits
11025 Hz sampling rate
'''