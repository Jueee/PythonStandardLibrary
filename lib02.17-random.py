'''
random 模块

random 模块包含许多随机数生成器.


标准库中提供的随机数生成器都是伪随机数生成器. 
不过这对于很多目的来说已经足够了, 比如模拟, 数值分析, 以及游戏. 
可以确定的是它不适合密码学用途.
'''
# 使用 random 模块获得随机数字
import random

for i in range(5):
	# random float: 0.0 <= number < 1.0
	print(random.random(),'=> ',end = '')
	# random float: 10 <= number < 20
	print(random.uniform(10,20), '=> ', end = '')
	# random integer: 100 <= number <= 1000
	print(random.randint(100,1000),'=> ' ,end = '')
	# random integer: even numbers in 100 <= number < 1000
	# randrange() 方法返回指定递增基数集合中的一个随机数，基数缺省值为1。
	# random.randrange ([start,] stop [,step])
	print(random.randrange(100, 1000,20))





# 使用 random 模块从序列取出随机项
# choice 函数, 它用来从一个序列里分拣出一个随机项目.
# 它可以用于列表, 元组, 以及其他序列(当然, 非空的).
import random

# random choice from a list
for i in range(5):
	print(random.choice([1,2,3,5,9]) ,' ' , end = '')
print('')





# 使用 random 模块打乱一副牌
# shuffle 函数可以用于打乱一个列表的内容 (也就是生成一个该列表的随机全排列).
import random

try:
	shuffle = random.shuffle
except AttributeError:
	def shuffle(x):
		for i in xrange(len(x)-1, 0, -1):
			j = int(random.random() * (i + 1))
			x[i], x[j] = x[j], x[i]
# range() 返回的是 “range object”，而不是实际的 list 值。
cards = list(range(52))
shuffle(cards)
myhand = cards[:5]
print(myhand)




# 使用 random 模块生成高斯分布随机数
# random 模块也包含了非恒定分布的随机生成器函数. 
# 使用了 gauss (高斯)函数来生成满足高斯分的布随机数字.
import random

histogram = [0] * 20

for i in range(100):
	i = int(random.gauss(5, 1) * 2)
	histogram[i] = histogram[i] + 1

# print the histogram
m = max(histogram)
print(type(histogram),m,histogram)
for v in histogram:
	# 字符串的乘法只支持int类型
	print('*' * int(v * 50 / m))

'''






****
*********************
**************************
******************************
***************************************
**************************************************
****************************
*************
****





'''


