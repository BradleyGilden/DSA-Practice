"""
implement bestSum with tabulation
"""

def bestSum(target, numbers):
    """Determine whether a list of numbers can sum up to the target value."""
    table = [None for _ in range(target + 1)]

    table[0] = []
    for i in range(target + 1):
        for j in numbers:
            if table[i] is not None and i + j <= target:
                if table[i + j] is None or (len(table[i]) + 1 < len(table[i + j])):
                    table[i + j] = table[i] + [j]

    return table[target]


if __name__ == '__main__':
    print(bestSum(7, [2, 3]))
    print(bestSum(7, [5, 3, 4, 7]))
    print(bestSum(7, [2, 4]))
    print(bestSum(8, [2, 3, 5]))
    print(bestSum(300, [7, 14]))
    print(bestSum(315, [25, 2, 3]))
