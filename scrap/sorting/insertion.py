#!/usr/bin/env python3

"""
Implementing a simple bubble sort

Author: Bradley Dillion Gilden
Date: 09-02-2024
"""


def insertionsort(arr):
    """sort an array using the bubble sort algorithm"""
    size = len(arr)
    # check if a swap was performed during bubbling

    for i in range(1, size):
        j = i
        while (j > 0 and arr[j] < arr[j - 1]):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        i += 1


if __name__ == '__main__':
    arr = [1, 4, 3, 20, 4, 19, 31, 2, 2]

    insertionsort(arr)

    print(arr)
