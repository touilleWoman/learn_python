
def cal(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
x = cal([1, 2, 3])
print (x)

# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
# *nums表示把nums这个list的所有元素作为可变参数传进去。
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。

def cal(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

x = cal(1, 2, 3)
print (x)



