#!/usr/bin/python3

"""
The Node class is for storing data and referencing other nodes.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


"""
The LinkedList class contains linked list methods to act on linked lists
"""


class LinkedList:

    def __init__(self):
        self.head = None
    
    def count_nodes(self):
        count = 0
        ptr = self.head
        while ptr is not None:
            ptr = ptr.next
            count += 1
        return count

    def print_list(self):
        if self.head is None:
            return None
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

    def add_beginning(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def add_end(self, data):
        new = Node(data)
        if self.head is None:
            return None

        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = new

    def add_pos(self, data, pos = 0):
        len = LinkedList.count_nodes(self)
        tracker = 1
        ptr = self.head
        
        if self.head is None or pos == 0:
            LinkedList.add_beginning(self, data)
            return
        elif pos > len - 1:
            LinkedList.add_end(self, data)
            return
        else:
            new_node = Node(data)
            while ptr.next is not None:
                if tracker == pos:
                    temp = ptr.next
                    ptr.next = new_node
                    new_node.next = temp
                ptr = ptr.next
                tracker += 1

