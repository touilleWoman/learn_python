def print_var(val):
	print("{} est de type {}".format(val, type(val)))

def my_var():
	print_var(42)
	print_var('42')
	print_var('quarente-deux')
	print_var(42.0)
	print_var(True)
	print_var([42])
	print_var({42: 42})
	print_var((42,))
	print_var(set())

if __name__ == '__main__':
	my_var()