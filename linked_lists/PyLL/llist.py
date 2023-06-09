#!/usr/bin/python3
class Node:

    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:

    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            return
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_node_beginning(self, data):
        new = Node(data)
        new.ref = self.head
        self.head = new

