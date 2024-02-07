#!/usr/bin/env python3

"""
Implement basic hashing with mod() using lists and tuples
Chaining is Implemented as well
Author: Bradley Dillion Gilden
Date: 05-02-2024
"""


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[(None, None)] for _ in range(100)]

    def __hash(self, key, h=0):
        for c in key:
            h += ord(c)
        return h % 100

    def __setitem__(self, key, val):
        h = self.__hash(key)
        if self.arr[h][0][0] is None:
            self.arr[h][0] = (key, val)

        elif not all(key != item[0] for item in self.arr[h]):
            for i in range(len(self.arr[h])):
                if key == self.arr[h][i][0]:
                    self.arr[h][i] = (key, val)
        else:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.__hash(key)
        if (self.arr[h][0][0] != key):
            for item in self.arr[h]:
                if item[0] == key:
                    return item[1]
        else:
            return self.arr[h][0][1]

    def __delitem__(self, key):
        h = self.__hash(key)
        if self.arr[h][0][0] is None:
            return
        for i, item in enumerate(self.arr[h]):
            if item[0] == key:
                del self.arr[h][i]
                break


if __name__ == '__main__':
    h = HashTable()
    h["cool"] = 1
    h["buy"] = 23
    h["food"] = 2039
    h["doof"] = 32
    h["doof"] = 22

    h["cool"] = 2
    del h["woah"]
    del h["doof"]
    print(h.arr)
    print(h["doof"])
    print(h["food"])
