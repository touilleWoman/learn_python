def kata00():
    t = (19, 42, 21)
    new_t = tuple(str(i) for i in t)
    print("The 3 numbers are: " + ', '.join(new_t))

if __name__ == '__main__':
    kata00()