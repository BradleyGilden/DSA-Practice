"""
Write a function `fib(n)` that takes in a number as an argument.
The function should return the n-th number of the Fibonacci sequence. Assume
'n' index starts at 1

sequence:
1 1 2 3 5 8 13 21 34 55 78 133
"""


def fib(n, memo={}):
    """return the n-th number of a fib sequence"""
    if memo.get(n):
        return memo[n]
    if n < 3:
        return 1
    # using dictionary to keep track of previous calls so that
    # we don't explore unecessary paths
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


if __name__ == '__main__':
    print(fib(3))
    print(fib(9))
    print(fib(50))
