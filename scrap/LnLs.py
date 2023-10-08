#!/usr/bin/python3

"""
contains linked lists in python

Author: Bradley Dillion Gilden
Date: 06-10-2023
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LnLs:

    def __init__(self):
        self.head = None

    def display(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end=" ")
            ptr = ptr.next
        print()

    def addstart(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new = Node(data)
            new.next = self.head
            self.head = new

    def addend(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = Node(data)

    @property
    def len(self):
        size = 0
        ptr = self.head
        while ptr is not None:
            size += 1
            ptr = ptr.next
        return size

    def iscyclic(self):

        if self.head is None:
            return False

        tortoise = self.head
        haire = self.head.next

        while haire:
            if tortoise is haire:
                return True
            tortoise = tortoise.next
            if haire.next is None:
                break
            else:
                haire = haire.next.next

        return False

    def tail(self):
        if self.head is None:
            return self.head
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            return ptr

    def reverse(self):
        if self.len <= 1:
            return
        behind = None
        current = self.head
        ahead = self.head.next

        while ahead is not None:
            current.next = behind
            behind = current
            current = ahead
            ahead = ahead.next
        current.next = behind
        self.head = current


if __name__ == '__main__':
    ll = LnLs()
    ll.addstart(10)
    ll.addstart(11)
    ll.addstart(12)
    ll.addend(13)

    ll2 = LnLs()
    ll2.addend(0)
    ll2.addend(1)
    ll2.addend(2)
    ll2.tail().next = ll2.head

    print(ll.len)

    print(ll.iscyclic())
    print(ll2.iscyclic())

    ll.display()
    ll.reverse()
    ll.display()
