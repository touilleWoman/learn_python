import sys


def rev_alpha(str):
    rev = ''.join(reversed(str))
    new_str = ""
    for elem in rev:
        if elem.isupper():
            elem = elem.lower()
        elif  elem.islower():
            elem = elem.upper()
        new_str += elem
    print(new_str)


def check_arg():
    if len(sys.argv) >= 2:
        lst = list()
        for x in range(1, len(sys.argv)):
            lst.append(sys.argv[x])
        str = ' '.join(lst)
        rev_alpha(str)


if __name__ == '__main__':
    check_arg()
