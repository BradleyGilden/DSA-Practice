#!/usr/bin/python3

"""
implements bubble sort

Author: Bradley Dillion Gilden
Date: 08-10-2023
"""


def bubble_sort(unsorted):
    """bubble sort algorithm"""
    size = len(unsorted)
    arr = unsorted[:]
    for i in range(size):
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    unsorted = [23, 56, 12, 34, 8, 27, 30, 42, 18, 20, 45, 9, 15, 21]
    print(unsorted)
    print(bubble_sort(unsorted))
