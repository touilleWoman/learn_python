import sys
import string

def filter(text, n):
    lst = [i.strip(string.punctuation) for i in text.split(' ')
    if len(i.strip(string.punctuation)) > n]
    print(lst)

def check_arg():
    if (len(sys.argv) == 3 and
        sys.argv[2].isdigit() and
        not sys.argv[1].isdigit()):
        filter(sys.argv[1], int(sys.argv[2]))
    else:
        print("ERROR")

if __name__ == '__main__':
    check_arg()