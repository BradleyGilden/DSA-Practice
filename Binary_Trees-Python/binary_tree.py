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

    def pre_order(self):
        """ performs pre-order traversal on a binary tree
        """
        def pre_order_traversal(node=self.root):
            if node is not None:
                print(node.data, end=" ")
                pre_order_traversal(node.left)
                pre_order_traversal(node.right)
        pre_order_traversal()
        print()

    def in_order(self):
        """ Performs in-order traversal on a binary tree
        """
        def in_order_traversal(node=self.root):
            if node is not None:
                in_order_traversal(node.left)
                print(node.data, end=" ")
                in_order_traversal(node.right)
        in_order_traversal()
        print()

    def post_order(self):
        """ performs post-order traversal on a binary tree
        """
        def post_order_traversal(node=self.root):
            if node is not None:
                post_order_traversal(node.left)
                post_order_traversal(node.right)
                print(node.data, end=" ")
        post_order_traversal()
        print()

    def count(self):
        """ counts number of nodes in a binary tree
        """
        counter = [0]

        def node_count(node=self.root):
            if (node is not None):
                counter[0] += 1
                node_count(node.left)
                node_count(node.right)
        node_count()
        return counter[0]

    def print(self):
        """ prints binary tree at 180 degrees
        """
        def printTree(node, level):
            if node is not None:
                printTree(node.right, level + 1)
                print(' ' * 4 * level + '-> ' + str(node.data))
                printTree(node.left, level + 1)
        printTree(self.root, 0)
