"""
Write a function `canSum(targetSum, numbers)`, that takes in a targetSum and
an array of numbers as arguments.

The function should return a boolean indicating whether or not it is possible
to generate the targetSum using numbers from the array

You may use an element of the array as many times as needed

You may assume that all input numbers are non-negative
"""


def canSum(targetSum, numbers, memo=None):
    """Determine whether a list of numbers can sum up to the target value."""
    if memo is None:
        memo = {}
    if memo.get(targetSum) is not None:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for n in numbers:
        remainder = targetSum - n
        if canSum(remainder, numbers, memo):
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False


if __name__ == '__main__':
    print(canSum(7, [2, 3]))  # true
    print(canSum(7, [5, 3, 4, 7]))  # true
    print(canSum(7, [2, 4]))  # false
    print(canSum(8, [2, 3, 5]))  # true
    print(canSum(300, [7, 14]))  # false


"""
m = target sum
n = array length

Brute Force Solution
--------------------
O(n^m) time
O(m) space

Brute Force Solution
--------------------
O(n * m) time
O(m) space
"""
