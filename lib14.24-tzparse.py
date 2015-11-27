'''
tzparse 模块

(已废弃) tzparse 模块用于解析时区标志( time zone specification ). 导入
时它会自动分析 TZ 环境变量.
'''

import os

print(dir(os.environ))
if not os.environ.get("TZ"):
	# set it to something...
	os.environ["TZ"] = "EST+5EDT;100/2,300/2"

# importing this module will parse the TZ variable
import tzparse

print("tzparams", "=>", tzparse.tzparams)
print("timezone", "=>", tzparse.timezone)
print("altzone", "=>", tzparse.altzone)
print("daylight", "=>", tzparse.daylight)
print("tzname", "=>", tzparse.tzname)