from sys import stderr
from typing import Union


class Node:
    def __init__(self, data, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self, data=None) -> None:
        if data:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.head = None
            self.tail = None

    def push(self, *args) -> None:
        """adds node/s at the beginning"""
        for item in args:
            new = Node(item)
            new.next = self.head
            if (self.head):
                self.head.prev = new
            else:
                self.tail = new
            self.head = new

    def append(self, *args) -> None:
        """adds node/s at the end"""
        for item in args:
            new = Node(item)
            if (self.tail):
                self.tail.next = new
            else:
                self.head = new
            new.prev = self.tail
            self.tail = new

    def print(self) -> None:
        """prints linked list"""
        ptr = self.head
        if ptr:
            print("← ", end="")
        while ptr:
            if (ptr.next is None):
                print(ptr.data, "→")
            else:
                print(ptr.data, end=" ⇄ ")
            ptr = ptr.next

    def print2(self) -> None:
        """prints linked list relationship vertically"""
        ptr = self.head
        while ptr:
            if (ptr is self.head and ptr.next):
                print(f"← {ptr.data} → {ptr.next.data}")
            elif (ptr is self.head):
                print(f"← {ptr.data} →")
            elif (ptr is self.tail):
                print(f"{ptr.data} →")
            else:
                print(f"{ptr.prev.data} ← {ptr.data} → {ptr.next.data}")
            ptr = ptr.next

    @property
    def len(self) -> int:
        """calculates length of a linked list"""
        count = 0
        ptr = self.head
        while ptr:
            count += 1
            ptr = ptr.next
        return count

    def addIndex(self, data, index):
        """adds node at given index"""
        length = self.len
        if (index > length):
            print("Index out of range", file=stderr)
            return
        elif (index == 0 or self.head is None):
            self.push(data)
            return
        elif (index == length):
            self.append(data)
            return

        i = 0
        ptr = self.head
        while (i < index - 1):
            ptr = ptr.next
            i += 1
        new = Node(data)
        new.next = ptr.next
        new.prev = ptr
        ptr.next.prev = new
        ptr.next = new

    def swap(self, n1, n2):
        """swaps 2 nodes in the list"""
        if (n1.next is n2):
            """"""
            prev = n1.prev
            n1.prev = n2
            n1.next = n2.next
            n2.prev = prev
            n2.next = n1
            if (prev):
                prev.next = n2
            if (n1.next):
                n1.next.prev = n1
        else:
            prev = n1.prev
            next = n1.next

            n1.next = n2.next
            n1.prev = n2.prev
            if (n2.next):
                n2.next.prev = n1
            if (n2.prev):
                n2.prev.next = n1

            n2.next = next
            n2.prev = prev
            if (prev):
                prev.next = n2
            if (next):
                next.prev = n2

        # rectifying head and tail
        if (self.head is n1):
            self.head = n2
        elif (self.head is n2):
            self.head = n1
        if (self.tail is n1):
            self.tail = n2
        elif (self.tail is n2):
            self.tail = n1

    # forward reference for return type
    def clone(self) -> Union['LinkedList', None]:
        """returns pointer to a clone of current list"""
        temp = None
        llcpy = None
        copy = None
        if (self.head is None):
            return None
        ptr = self.head
        while (ptr):
            # if list has not been initiated, initiate with LinkedList()
            if (not copy):
                llcpy = LinkedList(ptr.data)
                # keep track of head
                copy = llcpy.head
            else:
                # if list is established, just create new nodes
                copy = Node(ptr.data)
            if (temp):
                temp.next = copy
                copy.prev = temp
            if (ptr.next is None):
                llcpy.tail = copy
            temp = copy
            ptr = ptr.next
        return llcpy

    def delete(self, index) -> int:
        """delete a node at a specific index in the linked list"""
        if (self.head is None):
            return
        size = self.len
        if (index >= size or index < 0):
            print("index out of range", file=stderr)
        ptr = self.head
        i = 0
        data = None
        while (i <= index):
            if (i == index):
                data = ptr.data
                if (ptr is self.head and ptr is self.tail):
                    self.head = None
                    self.tail = None
                if (ptr is self.tail):
                    self.tail = ptr.prev
                if (ptr is self.head):
                    self.head = ptr.next

                if (ptr.prev):
                    ptr.prev.next = ptr.next
                if (ptr.next):
                    ptr.next.prev = ptr.prev
                ptr.next = None
                ptr.prev = None
                break
            ptr = ptr.next
            i += 1
        return data

    def bubble_sort(self):
        """implements bubble sort on linked list"""
        i = self.head
        swapped = True
        while (i and swapped):
            j = self.head
            swapped = False
            while (j.next):
                if (j.data > j.next.data):
                    self.swap(j, j.next)
                    j = j.prev
                    swapped = True
                j = j.next
            i = i.next

    def sorted_insert(self, val: int):
        """inserts a node into a sorted linked list"""

        ptr = self.head
        node = Node(val)

        # if list is empty
        if (self.head is None):
            self.head = node
            return

        while (ptr):
            if (node.data <= ptr.data):
                if (ptr is self.head):
                    self.head = node
                node.next = ptr
                if (ptr.prev):
                    ptr.prev.next = node
                node.prev = ptr.prev
                ptr.prev = node
                break
            elif (ptr.next is None and node.data > ptr.data):
                if (ptr is self.tail):
                    self.tail = node
                ptr.next = node
                node.prev = ptr
                break
            ptr = ptr.next
