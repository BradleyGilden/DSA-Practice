"""
Implement canSum with tabulation, assuming canSum(0, [*]) = true
"""

def canSum(target, numbers):
    # create table

    table = [False for _ in range(target + 1)]

    table[0] = True
    for i in range(target + 1):
        for j in numbers:
            if table[i] and i + j <= target:
                table[i + j] = True

    return table[target]


if __name__ == '__main__':
    print(canSum(7, [2, 3]))  # true
    print(canSum(7, [5, 3, 4, 7]))  # true
    print(canSum(7, [2, 4]))  # false
    print(canSum(8, [2, 3, 5]))  # true
    print(canSum(300, [7, 14]))  # false
