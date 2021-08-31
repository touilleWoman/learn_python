# Subject:
# A number spiral is an infinite grid whose upper-left square has number 1. Here are the first five layers of the spiral:

#  1  2  9 10 25
#  4  3  8 11 24
#  5  6  7 12 23
# 16 15 14 13 22
# 17 18 19 20 21

# Your task is to find out the number in row y and column x.

# Input:

# The first input line contains an integer t
# t: the number of tests.

# After this, there are t lines, each containing integers y and x.

# Output

# For each test, print the number in row y and column x.


# Example

# Input:
# 3
# 2 3
# 1 1
# 4 2

# Output:
# 8
# 1
# 15


def solve(y, x):
    if y >= x:
        if y % 2 == 0:
            max_value = y * y
            print(max_value - x + 1)
        else:
            min_value = (y - 1) * (y - 1) + 1
            print(min_value + x - 1)

    else:
        if x % 2 != 0:
            max_value = x * x
            print(max_value - y + 1)
        else:
            min_value = (x - 1) * (x - 1) + 1
            print(min_value + y - 1)


def main():
    t = int(input())
    for _ in range(t):
        y, x = map(int, input().split(" "))
        solve(y, x)


if __name__ == "__main__":
    main()
