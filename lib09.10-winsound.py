'''
winsound 模块

(只用于 Windows ) winsound 模块允许你在 Winodws 平台上播放 Wave 文件.
'''
import winsound

file = 'samples/sample.wav'

winsound.PlaySound(file, winsound.SND_FILENAME|winsound.SND_NOWAIT,)


'''
flag 变量说明:
•  SND_FILENAME - sound 是一个 wav 文件名
•  SND_ALIAS - sound 是一个注册表中指定的别名
•  SND_LOOP - 重复播放直到下一次 PlaySound ; 必须指定 SND_ASYNC
•  SND_MEMORY - sound 是一个 wav 文件的内存映像
•  SND_PURGE - 停止指定 sound 的所有实例
•  SND_ASYNC - 异步播放声音, 声音开始播放后函数立即返回
•  SND_NODEFAULT - 找不到 sound 时不播放默认的 beep 声音
•  SND_NOSTOP - 不打断当前播放中的任何 sound
•  SND_NOWAIT - sound 驱动忙时立即返回
'''

