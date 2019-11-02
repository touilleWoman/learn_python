import sys

def	reverse_dict(di):
	new_d = dict()
	for key in di:
		new_d[di[key]] = key
	return new_d

def find_state(city):
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
	if city in citys2:
		print(states2[citys2[city]])
	else:
		print("Unknown capital city")


def check_arg():
	if len(sys.argv) == 2:
		city_lst = sys.argv[1].split(',')
		for key in city_lst:
			string = city_lst[key]
			city_lst[key] = string.strip()

		print(city_lst)


if __name__ == '__main__':
	check_arg()
