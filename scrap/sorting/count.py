#!/usr/bin/env python3

"""
Implementing a counting sort

Author: Bradley Dillion Gilden
Date: 09-02-2024
"""


def count_sort(arr):
    """sort an array using the counting sort algorithm"""
    maxi = max(arr)
    counter = [0 for _ in range(maxi + 1)]
    csize = len(counter)

    # counting
    for num in arr:
        counter[num] += 1

    # acummalate values
    for i in range(1, csize):
        counter[i] += counter[i - 1]

    copy = arr.copy()

    # place according to counting array
    for num in copy:
        arr[counter[num] - 1] = num
        counter[num] -= 1


if __name__ == '__main__':
    arr = [1, 4, 3, 2, 4, 0, 3, 0, 2]
    count_sort(arr)
    print(arr)
