#! /usr/bin/env python3

print('Enter sapin\'s height')
height = int(input())
for i in range(height):
    for j in range(height - i -1):
        print(' ', end='')
    for j in range(i + 1):
        print(' *', end='')
    print()
#    print(" " * (height - i - 1) + '* ' * (i+1))
print(' ' * (height//2) + "||")

for i in range(4):
    if i==1:
        print("  *")
    if i==2:
        print(" * *")
    if i==3:
        print("* * *")
print(' ||')
