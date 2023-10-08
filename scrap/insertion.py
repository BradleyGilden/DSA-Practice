#!/usr/bin/python3

"""
implements insertion sort

Author: Bradley Dillion Gilden
Date: 08-10-2023
"""


def insertion_sort(unsorted):
    """bubble sort algorithm"""
    size = len(unsorted)
    arr = unsorted[:]
    for i in range(1, size):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


if __name__ == '__main__':
    unsorted = [23, 56, 12, 34, 8, 27, 30, 42, 18, 20, 45, 9, 15, 21]
    print(unsorted)
    print(insertion_sort(unsorted))
