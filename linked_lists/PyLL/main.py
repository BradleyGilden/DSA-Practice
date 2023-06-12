#!/usr/bin/python3
from llist import LinkedList


if __name__ == '__main__':
    list1 = LinkedList()
    list1.add_beginning("beg1")  # pos 1
    list1.add_beginning("beg2")  # pos 0
    list1.add_end("end1")  # pos 2
    list1.add_end("end2")  # pos 3
    list1.add_pos("pos1", 1) # new pos 1
    list1.print_list()
