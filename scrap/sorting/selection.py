#!/usr/bin/env python3

"""
Implementing a simple selection sort

Author: Bradley Dillion Gilden
Date: 09-02-2024
"""


def selection_sort(arr):
    """sort an array using the selection sort algorithm"""
    size = len(arr)
    for i in range(size):
        # find the index of the minimum value, by default, the minimum value is
        # the first index of the search range
        minidx = i
        for j in range(i, size):
            minidx = j if arr[j] < arr[minidx] else minidx
        arr[i], arr[minidx] = arr[minidx], arr[i]


if __name__ == '__main__':
    arr = [1, 4, 3, 20, 4, 19, 31, 2, 2]

    selection_sort(arr)

    print(arr)
