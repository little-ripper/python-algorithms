from random import randrange
from utils import performance


@performance
def _func_0(size: int):
    seq = [randrange(10**10) for i in range(size)]
    dd = float('inf')
    for x in seq:
        for y in seq:
            if x == y:
                continue
            d = abs(x-y)
            if d < dd:
                xx, yy, dd = x, y, d
    return xx, yy


@performance
def _func_1(size: int):
    seq = [randrange(10**10) for i in range(size)]
    seq.sort()
    dd = float('inf')
    for i in range(len(seq)-1):
        x, y = seq[i], seq[i+1]
        if x == y:
            continue
        d = abs(x-y)
        if d < dd:
            xx, yy, dd = x, y, d
    return xx, yy


def main():
    _func_0(size=100)
    _func_0(size=1000)
    _func_0(size=10000)
    _func_1(size=100)
    _func_1(size=1000)
    _func_1(size=10000)


if __name__ == '__main__':
    main()

main()
