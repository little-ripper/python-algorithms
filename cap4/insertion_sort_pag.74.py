from random import randrange
from helper.utils import performance


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


def _selection_sort_recursive(seq, i):
    if i == 0:
        return
    max_j = i
    for j in range(i):
        if seq[j] > seq[max_j]:
            max_j = j
    seq[i], seq[max_j] = seq[max_j], seq[i]
    _selection_sort_recursive(seq, i-1)


@performance
def selection_sort_recursive(seq):
    _selection_sort_recursive(seq, len(seq) - 1)


@performance
def selection_sort(seq):
    for i in range(len(seq)-1, 0, -1):
        max_j = i
        for j in range(i):
            if seq[j] > seq[max_j]:
                max_j = j
        seq[i], seq[max_j] = seq[max_j], seq[i]


def main():
    seq = [randrange(1, 10) for _ in range(10)]
    print(seq)
    insertion_sort_recursive(seq)
    print(seq)
    seq = [randrange(1, 10) for _ in range(10)]
    print(seq)
    insertion_sort(seq)
    print(seq)
    seq = [randrange(1, 10) for _ in range(10)]
    print(seq)
    selection_sort_recursive(seq)
    print(seq)
    seq = [randrange(1, 10) for _ in range(10)]
    print(seq)
    selection_sort(seq)
    print(seq)



main()
