import time
from tqdm import tqdm

def ft_progress(listy):
    for elem in tqdm(listy):
        yield elem

def demo():
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)

if __name__ == '__main__':
    demo()