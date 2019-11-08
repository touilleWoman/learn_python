class Vector():
    """docstring for Vector"""
    def __init__(self, arg):
        if isinstance(arg, list) and all(isinstance(i, float) for i in arg):
            self.values = arg
            self.length = len(arg)
        elif isinstance(arg, int):
            self.values = [float(i) for i in range(arg)]
            self.length = arg
        else:
            print('input error')
            exit()

    def __str__(self):
        return str(self.values)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return "(Vector multiple result {0})".format([ i * other for i in self.values])

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return ([ i + other for i in self.values])

    def __radd__(self, other):
        return  Vector.__add__(self, other)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return [ i - other for i in self.values]

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return [ other - i for i in self.values]

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return [ i * other for i in self.values]

    def __rmul__(self, other):
        return Vector.__mul__(self, other)

    def __repr__(self):
        return self.values


