import datetime

def kata02():
    t = (3,30,2019,9,25)
    d = datetime.datetime(t[2], t[3], t[4], t[0], t[1])
    print(d.strftime("%d/%m/%Y %H:%M"))


if __name__ == '__main__':
    kata02()