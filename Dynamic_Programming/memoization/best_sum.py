"""
Write a function `bestSUm(targetSum, numbers)` that takes in a targetSum
and an array of numbers as arguments

the funciton should return an array containing the sortest combination of
numbers that add up to exactly the targetSum

if there is a tie for the shorted, return any on of the shortest
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

    # initialize targetSum to None
    memo[targetSum] = None

    for n in numbers:
        remainder = targetSum - n
        combination = howSum(remainder, numbers, memo)
        if combination is not None:
            newcomb = [*combination, n]
            # check if targetSum has been memoized
            # if not, apply a new combination related to the target sub
            if memo[targetSum] is None:
                memo[targetSum] = newcomb
            # if it has been memoized, determine the smallest combination
            else:
                memo[targetSum] = (newcomb if
                                   len(newcomb) < len(memo[targetSum])
                                   else memo[targetSum])

    return memo[targetSum]


if __name__ == '__main__':
    print(howSum(7, [2, 3]))
    print(howSum(7, [5, 3, 4, 7]))
    print(howSum(7, [2, 4]))
    print(howSum(8, [2, 3, 5]))
    print(howSum(300, [7, 14]))
    print(howSum(315, [25, 2, 3]))


"""
m = target sum
n = array length

Brute Force Solution
--------------------
O(n^m * m) time
O(m) space

Brute Force Solution
--------------------
O(n * m^2) time
O(m^2) space
"""
