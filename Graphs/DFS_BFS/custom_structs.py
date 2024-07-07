from typing import Iterable


class Stack(list):
    def __init__(self, object: Iterable):
        super().__init__(object)

    def push(self, object):
        self.append(object)


class Queue:
    def __init__(self, ini=[]):
        if ini is None:
            self.__queue = []
        elif hasattr(ini, '__iter__'):
            self.__queue = list(ini)
        else:
            self.__queue = [ini]

    def enqueue(self, object):
        self.__queue.insert(0, object)

    def dequeue(self):
        return self.__queue.pop()

    def __str__(self):
        return f"[{', '.join(map(str, self.__queue))}]"
