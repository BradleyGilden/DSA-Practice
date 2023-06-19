"""
Implementing stacks with Doubly linked lists
"""


class Node:
    def __init__(self, data):  # constructor assigns data to var: data
        self.data = data
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def isEmpty(self):
        if self.__head is None:
            print("Empty")
        else:
            print("Not Empty")

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.__head
        if self.__head is not None:
            self.__head.prev = new_node
        new_node.prev = None
        self.__head = new_node
        self.__size += 1

    def view(self):
        ptr = self.__head
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

    def pop(self):
        if self.__head is None:
            return None

        ptr = self.__head
        self.__head = self.__head.next
        if self.__head is not None:
            self.__head.prev = None
        self.__size -= 1
        return ptr

    def peek(self):
        if self.__head is not None:
            return self.__head.data
        else:
            print("Stack is empty")

    def get_size(self):
        return self.__size
