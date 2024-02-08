#!/usr/bin/env python3

"""
Implementing hashmap with linked list
Author: Bradley Dillion Gilden
Date: 06-02-2024
"""
from colored import Fore, Back, Style
r = Style.reset


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
        return (h % 100) + 1

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
        colors = Back.black + Fore.green
        y = Fore.yellow
        o = Fore.orange_1
        t = Fore.TAN
        ptr = self.head
        print(f"{colors}<id>[key, val] -chaining-> (key,val){r}\n")
        while (ptr):
            if (ptr.key is not None):
                print(f"{o}<{ptr.idx}>",
                      f"{r}[{t}{ptr.key}{r}, {o}{ptr.val}{r}]",
                      end=f"{y} -> {r}",
                      sep="")
                if (ptr.snext):
                    ptr2 = ptr.snext
                    while (ptr2):
                        print(f"{r}({t}{ptr2.key}{r}, {o}{ptr2.val}{r})",
                              end=f"{y} -> {r}")
                        ptr2 = ptr2.snext
                print()
            ptr = ptr.dnext

    def __getitem__(self, key):
        h = self.__hash(key)
        if (h > 50):
            print("used tail for search")
            ptr = self.tail
            while (ptr):
                if (ptr.idx == h and ptr.key == key):
                    return ptr.val
                elif (ptr.idx == h):
                    ptr = ptr.snext
                    while (ptr):
                        if (ptr.key == key):
                            return key
                        ptr = ptr.snext
                ptr = ptr.dprev
        else:
            print("used head for search")
            ptr = self.head
            while (ptr):
                if (ptr.idx == h and ptr.key == key):
                    return ptr.val
                elif (ptr.idx == h):
                    ptr = ptr.snext
                    while (ptr):
                        if (ptr.key == key):
                            return ptr.val
                        ptr = ptr.snext
                ptr = ptr.dnext

    def __delitem__(self, key):
        ptr = self.head
        h = self.__hash(key)

        while (ptr):
            if (ptr.idx == h and key == key):
                # if Index node has chained links tied to it
                # make chain node the new Index node
                if (ptr.snext):
                    new = IndexNode(ptr.snext.val, ptr.snext.key, ptr.idx)
                    if (ptr.dprev):
                        ptr.dprev.dnext = new
                    new.dprev = ptr.dprev
                    new.dnext = ptr.dnext
                    if (ptr.dnext):
                        ptr.dnext.prev = new
                    new.snext = ptr.snext.snext
                    ptr.snext = None
                else:  # delting a normal Index node with no chaings
                    if (ptr.dprev):
                        ptr.dprev.dnext = ptr.dnext
                    if (ptr.dnext):
                        ptr.dnext.dprev = ptr.dprev
                ptr.dnext = None
                ptr.dprev = None
                break
            elif (ptr.idx == h):
                # deleting a chain node
                ptr2 = ptr.snext
                while (ptr2):
                    if (ptr2.key == key):
                        ptr.snext = ptr2.snext
                        break
                    ptr = ptr2
                    ptr2 = ptr2.snext
            ptr = ptr.dnext


if __name__ == '__main__':
    h = HashTable()
    h["a"] = 97
    h["cool"] = 1
    h["cool"] = 2
    h["looc"] = 3
    h["buy"] = 23
    h["food"] = 2039
    h["doof"] = 32
    h["doof"] = 22
    h.print()
    print()
    print("doof:", h["doof"])
    print()
    print("a:", h["a"])
    del h["a"]
    del h["food"]
    print()
    h.print()
