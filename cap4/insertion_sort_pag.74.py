from random import randrange
from python_algorithms.utils import performance


def _insertion_sort_recursive(seq, i):
    if i == 0:
        return
    _insertion_sort_recursive(seq, i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1


@performance
def insertion_sort_recursive(seq):
    _insertion_sort_recursive(seq, len(seq) - 1)


@performance
def insertion_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1


def main():
    seq = [randrange(1, 10) for _ in range(10)]
    print(seq)
    insertion_sort_recursive(seq)
    print(seq)
    seq = [randrange(1, 10) for _ in range(10)]
    print(seq)
    insertion_sort(seq)
    print(seq)

main()
