import sys

def	reverse_dict(di):
	new_d = dict()
	for key in di:
		new_d[di[key]] = key
	return new_d

def find(val):
	states = {
	"Oregon"    : "OR",
	"Alabama"   : "AL",
	"New Jersey": "NJ",
	"Colorado"  : "CO"
	}

	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}

	states2 = reverse_dict(states)
	citys2 = reverse_dict(capital_cities)
	val2 = case_edit(val)

	if val2 in citys2:
		print(val2, 'is the capital of', states2[citys2[val2]])
	elif val2 in states:
		print(capital_cities[states[val2]], 'is the capital of', val2)
	else:
		print(val, "is neither a capital city nor a state")

def case_edit(val):
	val = val.lower()
	val = val.capitalize()
	for i in range(0, len(val)):
		if val[i] == ' ':
			val = val[:(i + 1)] + val[i + 1].upper() + val[(i + 2):]
	return(val)

def check_arg():
	if len(sys.argv) == 2:
		city_lst = sys.argv[1].split(',')
		city_lst = [i.strip() for i in city_lst]
		for val in city_lst:
			if val != "":
				find(val)

if __name__ == '__main__':
	check_arg()
