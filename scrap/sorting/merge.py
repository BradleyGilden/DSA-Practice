#!/usr/bin/env python3

"""
Implementing a recursive merge sort

Author: Bradley Dillion Gilden
Date: 09-02-2024
"""


def merge(left, right, arr):
    """merges left and right sub lists"""
    i, j, k = 0, 0, 0
    lsize = len(left)
    rsize = len(right)

    while (i < lsize and j < rsize):
        if (left[i] < right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while (i < lsize):
        arr[k] = left[i]
        i += 1
        k += 1

    while (j < rsize):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr):
    """sort an array using the insertion sort algorithm"""
    size = len(arr)

    # base case
    if size < 2:
        return

    mid = size // 2

    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, arr)


if __name__ == '__main__':
    arr = [1, 4, 3, 20, 4, 19, 31, 2, 2]

    merge_sort(arr)

    print(arr)
