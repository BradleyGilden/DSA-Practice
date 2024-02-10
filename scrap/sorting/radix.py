#!/usr/bin/env python3

"""
Implementing a counting sort

Author: Bradley Dillion Gilden
Date: 09-02-2024
"""


def count_sort(arr, modulator, unit):
    """sort an array using the counting sort algorithm"""
    counter = [0 for _ in range(10)]
    csize = len(counter)

    # counting
    for num in arr:
        num = (num % modulator) // unit
        counter[num] += 1

    # acummalate values
    for i in range(1, csize):
        counter[i] += counter[i - 1]

    copy = arr.copy()
    ccopy = counter.copy()

    # shifting
    for i in range(1, csize):
        counter[i] = ccopy[i - 1]

    counter[0] = 0

    # place according to counting array
    for num in copy:
        inum = (num % modulator) // unit
        arr[counter[inum]] = num
        counter[inum] += 1


def radix_sort(arr):
    """implements counting sort on individual units of a number list"""
    digits = len(str(max(arr)))
    modulator = 10

    for _ in range(digits):
        count_sort(arr, modulator, modulator // 10)
        modulator *= 10


if __name__ == '__main__':
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    radix_sort(arr)
    print(arr)
