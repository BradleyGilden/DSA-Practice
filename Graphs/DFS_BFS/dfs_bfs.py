"""
DEPTH FIRST SEARCH (using Graph 1 from the README)
"""
from custom_structs import Stack, Queue  # noqa


if __name__ == '__main__':
    que = Stack([5, 3, 4])
    print(que)
    que.push(6)
    print(que)
    print(que.pop())
    print(que)
