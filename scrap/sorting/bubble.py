#!/usr/bin/env python3

"""
Implementing a simple bubble sort

Author: Bradley Dillion Gilden
Date: 09-02-2024
"""


def bubblesort(arr):
    """sort an array using the bubble sort algorithm"""
    size = len(arr)
    i = 0
    # check if a swap was performed during bubbling
    has_swapped = True

    while i < size and has_swapped:
        has_swapped = False
        for j in range(size - i - 1):
            if (arr[j + 1] < arr[j]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                has_swapped = True
        i += 1


if __name__ == '__main__':
    arr = [1, 4, 3, 20, 4, 19, 31, 2, 2]

    bubblesort(arr)

    print(arr)
