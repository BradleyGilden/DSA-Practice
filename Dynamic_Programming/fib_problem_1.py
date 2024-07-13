"""
Write a function `fib(n)` that takes in a number as an argument.
The function should return the n-th number of the Fibonacci sequence. Assume
'n' index starts at 1

sequence:
1 1 2 3 5 8 13 21 34 55 78 133
"""


def fib(n, memory={}):
    """return the n-th number of a fib sequence"""

    if n < 3:
        return 1

    # using dictionary to keep track of previous calls so that we don't explore unecessary paths
    fib1 = fib(n - 1, memory) if not memory.get(n - 1) else memory[n - 1]
    fib2 = fib(n - 2, memory) if not memory.get(n - 2) else memory[n - 2]
    val = fib1 + fib2
    memory[n] = val
    return val


if __name__ == '__main__':
    print(fib(3))
    print(fib(9))
    print(fib(50))
