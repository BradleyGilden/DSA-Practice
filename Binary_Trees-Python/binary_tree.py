#!/usr/bin/python3

"""
This module contains the binary tree class for setting up binary trees

Author: Bradley Dillion Gilden
Date: 22-10-2023
"""

class Node:
    """represents nodes in a binary tree"""
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    """contains all the methods necessary for working on binary trees"""
    def __init__(self, rootVal):
        self.root = Node(rootVal)

    def add_left(self, data):
        self.left = Node(data)


if __name__ == '__main__':
