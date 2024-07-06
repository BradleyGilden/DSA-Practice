"""
DEPTH FIRST SEARCH (using Graph 1 from the README)
"""


from typing import Iterable


class Stack(list):
    def __init__(self, object: Iterable):
        super().__init__(object)


class Queue:
    def __init__(self, ini=None):
        if ini is None:
            self.__queue = []
        else:
            self.__queue = [ini]

    def enqueue(self, val):
        self.__queue.insert(0, val)

    def dequeue(self):
        return self.__queue.pop()
