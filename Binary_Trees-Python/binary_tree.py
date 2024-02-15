#!/usr/bin/python3

"""
This module contains the binary tree class for setting up binary trees

Author: Bradley Dillion Gilden
Date: 22-10-2023
"""


class Node:
    """represents nodes in a binary tree"""
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


class BinaryTree:
    """contains all the methods necessary for working on binary trees"""
    def __init__(self, data=None, left=None, right=None):
        self.root = None
        if (data):
            self.root = Node(data)

    def print(self):
        def printTree(node, level):
            if node is not None:
                printTree(node.right, level + 1)
                print(' ' * 4 * level + '-> ' + str(node.data))
                printTree(node.left, level + 1)
        printTree(self.root, 0)
