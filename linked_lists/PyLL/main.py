#!/usr/bin/python3
from linkedlist import LinkedList


if __name__ == '__main__':
    list1 = LinkedList()
    list1.add_end("item1")
    list1.add_end("item2")
    list1.add_end("item3")
    list1.reverse()
    list1.print_list()
