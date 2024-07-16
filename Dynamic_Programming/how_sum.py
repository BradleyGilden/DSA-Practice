"""
Write a function `howSum(targetSum, numbers)` that takes in a targetSum
and an array of numbers as arguments.

The function should return an array containing any combination of elemnets
that add up to exactly the targetSum. If there is no combination that
adds up to the targetSum, then return null.

If there are multiple combinations possible, you may return any single one.
"""


def howSum(targetSum, numbers, memo=None):
    """Determine whether a list of numbers can sum up to the target value."""
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for n in numbers:
        remainder = targetSum - n
        combination = howSum(remainder, numbers, memo)
        if combination is not None:
            combination.append(n)
            memo[targetSum] = combination.copy()
            return combination

    memo[targetSum] = None
    return None


if __name__ == '__main__':
    print(howSum(7, [2, 3]))
    print(howSum(7, [5, 3, 4, 7]))
    print(howSum(7, [2, 4]))
    print(howSum(8, [2, 3, 5]))
    print(howSum(300, [7, 14]))
    print(howSum(315, [25, 2, 3]))
