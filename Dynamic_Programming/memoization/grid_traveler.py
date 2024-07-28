"""
Say that you are a traveler on a 2D grid. You begin in the top-left corner and
your goal is to move to the bottom-right corner. You may only move down or
right.
In how many ways can you travel to the goal on a grid with dimensions m * n?
"""


def gridTraveler(col, row, memo=None) -> int:
    """traverses grid with down and right directions"""
    # we use n - down and m - right because grid is shrinking

    if memo is None:
        memo = {}
    gsize = ','.join(sorted([str(col), str(row)]))

    if memo.get(gsize):
        return memo[gsize]

    # out of bounds
    if col == 0 or row == 0:
        return 0

    # bottom right target reached
    if col == 1 and row == 1:
        return 1

    memo[gsize] = 0
    memo[gsize] += (gridTraveler(col - 1, row, memo) +
                    gridTraveler(col, row - 1, memo))

    return memo[gsize]


if __name__ == '__main__':
    print(gridTraveler(4, 3))
    print(gridTraveler(100, 50))

"""
brute force version
------------------
O(2^(n + m)) time
O(n + m) space

memoized version
-----------------
O(m * n) time
O(n + m) space
"""
