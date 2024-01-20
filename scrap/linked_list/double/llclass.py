from sys import stderr


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
        """adds node at the beginning"""
        for item in args:
            new = Node(item)
            new.next = self.head
            if (self.head):
                self.head.prev = new
            else:
                self.tail = new
            self.head = new

    def append(self, *args) -> None:
        """adds node at the end"""
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
        ptr.next = new
