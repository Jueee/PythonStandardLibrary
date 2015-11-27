'''
time 模块

time 模块提供了一些处理日期和一天内时间的函数. 它是建立在 C 运行时库的简单封装.
给定的日期和时间可以被表示为浮点型(从参考时间, 通常是 1970.1.1 到现在经过的秒数. 即 Unix 格式), 或者一个表示时间的 struct (类元组).
'''

# 使用 time 模块获取当前时间
# localtime 和 gmtime 返回的类元组包括年, 月, 日, 时, 分, 秒, 星期, 一年的第几天, 日光标志. 
# 其中年是一个四位数(在有千年虫问题的平台上另有规定, 但还是四位数), 星期从星期一(数字 0 代表)开始, 1 月 1 日是一年的第一天.
import time
now = time.time()
print(now,'seconds since',time.gmtime(0)[:6])
print()
print('or in other words')
print('- local time', time.localtime(now))
print('- utc:',time.gmtime(now)) 
'''
1441525364.349176 seconds since (1970, 1, 1, 0, 0, 0)

or in other words
- local time time.struct_time(tm_year=2015, tm_mon=9, tm_mday=6, tm_hour=15, tm_min=42, tm_sec=44, tm_wday=6, tm_yday=249, tm_isdst=0)
- utc: time.struct_time(tm_year=2015, tm_mon=9, tm_mday=6, tm_hour=7, tm_min=42, tm_sec=44, tm_wday=6, tm_yday=249, tm_isdst=0)
'''

'''
将时间值转换为字符串
'''
# 使用 time 模块格式化时间输出
# 可以使用标准的格式化字符串把时间对象转换为字符串, 不过 time 模块已经提供了许多标准转换函数
import time
now = time.localtime(time.time())
print(time.asctime(now))
print(time.strftime("%y/%m/%d %H:%M", now))
print(time.strftime("%a %b %d", now))
print(time.strftime("%c", now))
print(time.strftime("%I %p", now))
print(time.strftime("%Y-%m-%d %H:%M:%S", now))
# do it by hand...
year,month, day, hour, minute, second, weekday, yearday, daylight = now
print("%04d-%02d-%02d" % (year, month, day))
print("%02d:%02d:%02d" % (hour, minute, second))
print(("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")[weekday], yearday)
'''
Sun Sep  6 15:48:17 2015
15/09/06 15:48
Sun Sep 06
09/06/15 15:48:17
03 PM
2015-09-06 15:48:17
2015-09-06
15:48:17
SUN 249
'''




'''
将字符串转换为时间对象
'''
# 使用 time.strptime 函数解析时间
# time 模块包含了 strptime 函数, 它的作用与 strftime 相反.
# 给定一个字符串和模式, 它返回相应的时间对象
import time
try:
	strptime = time.strptime
except AttributeError:
	from strptime import strptime

print(strptime('30 Nov 00','%d %b %y'))
print(strptime('1 Jan 70 1:30pm','%d %b %y %I:%M%p'))
'''
time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=13, tm_min=30, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=-1)
'''
print('-----------------')

# strptime 实现
# 对于没有提供标准实现的平台, 下面提供了一个不完全的实现.
import re
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
SPEC = {
	# map formatting code to a regular expression fragment
	"%a": "(?P<weekday>[a-z]+)",
	"%A": "(?P<weekday>[a-z]+)",
	"%b": "(?P<month>[a-z]+)",
	"%B": "(?P<month>[a-z]+)",
	"%C": "(?P<century>\d\d?)",
	"%d": "(?P<day>..?)",
	"%D": "(?P<month>\d\d?)/(?P<day>\d\d?)/(?P<year>\d\d)",
	"%e": "(?P<day>\d\d?)",
	"%h": "(?P<month>[a-z]+)",
	"%H": "(?P<hour>\d\d?)",
	"%I": "(?P<hour12>\d\d?)",
	"%j": "(?P<yearday>\d\d?\d?)",
	"%m": "(?P<month>\d\d?)",
	"%M": "(?P<minute>\d\d?)",
	"%p": "(?P<ampm12>am|pm)",
	"%R": "(?P<hour>\d\d?):(?P<minute>\d\d?)",
	"%S": "(?P<second>\d\d?)",
	"%T": "(?P<hour>\d\d?):(?P<minute>\d\d?):(?P<second>\d\d?)",
	"%U": "(?P<week>\d\d)",
	"%w": "(?P<weekday>\d)",
	"%W": "(?P<weekday>\d\d)",
	"%y": "(?P<year>\d\d)",
	"%Y": "(?P<year>\d\d\d\d)",
	"%%": "%"
}
class TimeParser:
	def __init__(self, format):
		# convert strptime format string to regular expression
		format = ' '.join(re.split("(?:\s|%t|%n)+", format))
		pattern = []
		try:
			for spec in re.findall("%\w|%%|.", format):
				if spec[0] == "%":
					spec = SPEC[spec]
				pattern.append(spec)
		except KeyError:
			raise(ValueError, "unknown specificer: %s" % spec)
		self.pattern = re.compile("(?i)" + "".join(pattern))
	def match(self, daytime):
		# match time string
		match = self.pattern.match(daytime)
		if not match:
			print(ValueError, "format mismatch")
		else:
			dic = match.groupdict()
			tm = [0] * 9
			# extract date elements
			y = dic.get("year")
			if y:
				y = int(y)
				if y < 68:
					y = 2000 + y
				elif y < 100:
					y = 1900 + y
				tm[0] = y
			m = dic.get("month")
			if m:
				if m in MONTHS:
					m = MONTHS.index(m) + 1
				tm[1] = int(m)
			d = dic.get("day")
			if d: tm[2] = int(d)
			# extract time elements
			h = dic.get("hour")
			if h:
				tm[3] = int(h)
			else:
				h = dic.get("hour12")
				if h:
					h = int(h)
					if string.lower(get("ampm12", "")) == "pm":
						h = h + 12
					tm[3] = h
			m = dic.get("minute")
			if m: tm[4] = int(m)
			s = dic.get("second")
			if s: tm[5] = int(s)
			# ignore weekday/yearday for now
			return tuple(tm)
def strptime(string, format="%a %b %d %H:%M:%S %Y"):
	return TimeParser(format).match(string)
if __name__ == "__main__":
	# try it out
	import time
	print(strptime("2000-12-20 01:02:03", "%Y-%m-%d %H:%M:%S"))
	print(strptime(time.ctime(time.time())))

'''
(2000, 12, 20, 1, 2, 3, 0, 0, 0)
(2015, 9, 6, 17, 3, 16, 0, 0, 0)
'''
print('-----------------')






'''
转换时间值

将时间元组转换回时间值非常简单, 至少我们谈论的当地时间 (local time)如此. 
'''

# 使用 time 模块将本地时间元组转换为时间值(整数)
# 只要把时间元组传递给 mktime 函数
import time
t0 = time.time()
tm = time.localtime(t0)
print(tm)
print(t0)
print(time.mktime(tm))
'''
time.struct_time(tm_year=2015, tm_mon=9, tm_mday=6, tm_hour=17, tm_min=8, tm_sec=29, tm_wday=6, tm_yday=249, tm_isdst=0)
1441530509.76903
1441530509.0
'''


# 将 UTC 时间元组转换为时间值(整数)
# timegm 函数，将 UTC 时间 (Universal Time,Coordinated: 特林威治标准时间)转换为时间值的函数
import time
def _d(y, m, d, days=(0,31,59,90,120,151,181,212,243,273,304,334,365)):
	# map a date to the number of days from a reference point
	return (((y - 1901)*1461)/4 + days[m-1] + d + ((m > 2 and not y % 4 and (y % 100 or not y % 400)) and 1))
def timegm(tm, epoch=_d(1970,1,1)):
	year, month, day, h, m, s = tm[:6]
	assert year >= 1970
	assert 1 <= month <= 12
	return (_d(year, month, day) - epoch)*86400 + h*3600 + m*60 + s
t0 = time.time()
tm = time.gmtime(t0)
print(tm)
print(t0)
print(timegm(tm))
'''
time.struct_time(tm_year=2015, tm_mon=9, tm_mday=6, tm_hour=9, tm_min=11, tm_sec=15, tm_wday=6, tm_yday=249, tm_isdst=0)
1441530675.63003
1441552275.0
'''
# calendar 模块提供了一个类似的函数 calendar.timegm .





'''
Timing 相关

time 模块可以计算 Python 程序的执行时间
'''
# 使用 time 模块评价算法
# 可以测量 "wall time" (real world time), 或是"进程时间" (消耗的 CPU 时间).
import time
def procedure():
	time.sleep(2.5)
# measure process time
# clock 函数通常测量从程序启动到测量时的 wall time.
t0 = time.clock()
procedure()
print(time.clock() - t0, 'seconds process time')
# measure wall time
t0 = time.time()
procedure()
print(time.time() - t0, 'seconds wall time')
'''
2.4993525509662984 seconds process time
2.500499963760376 seconds wall time
'''
