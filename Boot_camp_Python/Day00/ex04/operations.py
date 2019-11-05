import sys

def operations(x, y):
    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
        if y == 0:
            div = "ERROR (div by zero)"
            modulo = "ERROR (modulo by zero)"
        else:
            div = x / y
            modulo = x % y
        print("Sum:        ", x + y)
        print("Difference:", x - y)
        print("Product:     ", x * y)
        print("Quotient:    ", div)
        print("Remainder: ", modulo)
    else:
        print(  "InputError: only numbers\n"
                "Usage: python operations.py\n"
                "Example:\n"
                "   python operations.py 10 3"
                )

def check_arg():
    if len(sys.argv) < 3:
        print(  "Usage: python operations.py\n"
                "Example:\n"
                "   python operations.py 10 3")
    elif len(sys.argv) > 3:
        print(  "InputError: too many arguments\n"
                "Usage: python operations.py\n"
                "Example:\n"
                "   python operations.py 10 3")
    else:
        operations(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    check_arg()