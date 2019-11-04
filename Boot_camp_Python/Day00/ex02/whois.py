import sys

def check_arg():
    if len(sys.argv) == 2:
        if isinstance(sys.argv[1], int):
            print(int(sys.argv[1]))
        else:
            print("ERROR")
    else:
        print("ERROR")


if __name__ == '__main__':
    check_arg()