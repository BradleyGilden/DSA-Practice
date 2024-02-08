from sys import stderr


class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, data=None) -> None:
        if data:
            self.head = Node(data)
        else:
            self.head = None

    def push(self, *args) -> None:
        """adds node at the beginning"""
        for item in args:
            new = Node(item)
            new.next = self.head
            self.head = new

    def append(self, data) -> None:
        """adds node at the end"""
        ptr = self.head
        if not self.head:
            self.head = Node(data)
            return
        while ptr.next:
            ptr = ptr.next
        new = Node(data)
        ptr.next = new

    def print(self) -> None:
        """prints linked list"""
        ptr = self.head
        while ptr:
            if (ptr.next is None):
                print(ptr.data)
            else:
                print(ptr.data, end=" -> ")
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

    def is_cyclic(self):
        if (self.head is None):
            return

        slow = self.head
        fast = self.head.next

        while (fast and fast.next):
            if (slow == fast):
                return True
            slow = slow.next
            fast = fast.next.next
        return False
