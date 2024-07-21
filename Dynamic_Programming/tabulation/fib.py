"""
return number at index n given in fib(n) in the fibonacci sequence.

0th number is 0 in the sequence
1st number is 1 in the sequence
Hence sequence: 0, 1, 1, 2, 3, 5, 8, 13...
"""

def fib(n):

    table = [0, 1, *[0 for _ in range(n - 1)]]

    for i in range(2, len(table)):
        table[i] = table[i - 1] + table[i - 2]

    return table[n]

if __name__ == '__main__':
    print(fib(10))
    print(fib(3))
    print(fib(2))
    print(fib(1))
    print(fib(0))