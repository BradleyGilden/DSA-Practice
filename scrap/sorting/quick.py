#!/usr/bin/env python3

"""
Implementing a recursive merge sort

Author: Bradley Dillion Gilden
Date: 09-02-2024
"""


def partition(arr, low, high):
    """lomutos partition"""
    i = low - 1
    for j in range(low, high + 1):
        if j == high or arr[j] < arr[high]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # the new pivot
    return i


def quick_sort(arr, low, high):
    """sort an array using the insertion sort algorithm"""
    if (low < high):
        pivot = partition(arr, low, high)
        # call quick sort on left
        quick_sort(arr, low, pivot - 1)
        # call quick sort on right
        quick_sort(arr, pivot + 1, high)


if __name__ == '__main__':
    arr = [1, 4, 3, 20, 4, 19, 31, 2, 2]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
