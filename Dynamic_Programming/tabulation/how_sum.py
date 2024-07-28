"""
implement howSum with tabulation method
"""

def howSum(target, numbers):
    """Determine whether a list of numbers can sum up to the target value."""
    table = [None for _ in range(target + 1)]

    table[0] = []
    for i in range(target + 1):
        for j in numbers:
            if table[i] is not None and i + j <= target:
                table[i + j] = table[i] + [j]

    return table[target]


if __name__ == '__main__':
    print(howSum(7, [2, 3]))
    print(howSum(7, [5, 3, 4, 7]))
    print(howSum(7, [2, 4]))
    print(howSum(8, [2, 3, 5]))
    print(howSum(300, [7, 14]))
    print(howSum(315, [25, 2, 3]))
