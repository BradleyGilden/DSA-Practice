from typing import Iterable


class Stack(list):
    def __init__(self, object: Iterable):
        obj = object
        # check if object is iterable
        if not hasattr(object, '__iter__'):
            obj = [object]
        super().__init__(obj)

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
        return str(self.__queue)

    def __len__(self):
        return len(self.__queue)
