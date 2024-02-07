#!/usr/bin/env python3

"""
Implementing hashmap with linked list
Author: Bradley Dillion Gilden
Date: 06-02-2024
"""


class IndexNode:
    def __init__(self, value=None, key=None, idx=1):
        self.dprev = None
        self.idx = idx
        self.key = key
        self.val = value
        self.snext = None
        self.dnext = None


class ChainNode:
    def __init__(self, key=None, val=None):
        self.snext = None
        self.key = key
        self.val = val


class HashTable:
    __MAX = 100

    def __init__(self, max=__MAX):
        self.head = IndexNode()
        self.MAX = max if max >= 2 else HashTable.__MAX
        self.tail = IndexNode(idx=self.MAX)
        self.__build_index()

    def __hash(self, key, h=0):
        for c in key:
            h += ord(c)
        return h % 100

    def __build_index(self):
        """builds the index of the linked list"""
        temp = self.head
        for i in range(2, self.MAX):
            ptr = IndexNode(idx=i)
            temp.dnext = ptr
            ptr.dprev = temp
            if (i == self.MAX - 1):
                ptr.dnext = self.tail
                self.tail.dprev = ptr
                break
            temp = ptr

    def __setitem__(self, key, val):
        h = self.__hash(key)
        ptr = self.head

        while (ptr):
            if (ptr.idx == h):
                if (ptr.val is None):
                    ptr.val = val
                    ptr.key = key
                else:
                    while (ptr):
                        if (ptr.key == key):
                            ptr.val = val
                            break
                        elif (ptr.snext is None):
                            ptr.snext = ChainNode(val=val, key=key)
                            break
                        ptr = ptr.snext
                break
            ptr = ptr.dnext

    def print(self):
        """print hashmap"""
        ptr = self.head
        print(f"<id>[key, val] -chaining-> (key,val)\n")
        while (ptr):
            if (ptr.key is not None):
                print(f"<{ptr.idx}>[{ptr.key}, {ptr.val}]", end=" -> ")
                if (ptr.snext):
                    ptr2 = ptr.snext
                    while (ptr2):
                        print(f"({ptr2.key}, {ptr2.val})", end=" -> ")
                        ptr2 = ptr2.snext
                print()
            ptr = ptr.dnext

    # def __getitem__(self, key):
    #     h = self.__hash(key)
    #     if (self.arr[h][0][0] != key):
    #         for item in self.arr[h]:
    #             if item[0] == key:
    #                 return item[1]
    #     else:
    #         return self.arr[h][0][1]

    # def __delitem__(self, key):
    #     h = self.__hash(key)
    #     if self.arr[h][0][0] is None:
    #         return
    #     for i, item in enumerate(self.arr[h]):
    #         if item[0] == key:
    #             del self.arr[h][i]
    #             break


if __name__ == '__main__':
    h = HashTable()
    h["cool"] = 1
    h["cool"] = 2
    h["looc"] = 3
    h["buy"] = 23
    h["food"] = 2039
    h["doof"] = 32
    h["doof"] = 22
    h.print()
