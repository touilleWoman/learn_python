def read_file():
	f = open("numbers.txt", "r")
	str = f.read()
	return str

def print_nb():
	str = read_file()
	print(str.replace(",", "\n"))

if __name__ == '__main__':
	print_nb()