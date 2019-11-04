import sys

def odd_or_even(nb):
    if nb == 0:
        print("I'm Zero.")
    elif nb % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd.")

def check_arg():
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) == 2:
        string = sys.argv[1]
        if string.isdigit():
            odd_or_even(int(sys.argv[1]))
        else:
            print("ERROR")
    else:
        print("ERROR")

if __name__ == '__main__':
    check_arg()