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

    def level_order(self):
        """ performs level-order traversal on a binary tree
        """
        height = self.height(self.root)

        def print_level(level, node=self.root, count=0):
            if node is not None:
                if level == count:
                    print(node.data, end=" ")
                print_level(level, node.left, count + 1)
                print_level(level, node.right, count + 1)

        for i in range(height + 1):
            print_level(i)
        print()

    def rlevel_order(self):
        """ performs reverse level-order traversal on a binary tree
        """
        height = self.height(self.root)

        def print_level(level, node=self.root, count=0):
            if node is not None:
                if level == count:
                    print(node.data, end=" ")
                print_level(level, node.right, count + 1)
                print_level(level, node.left, count + 1)

        for i in range(height + 1, -1, -1):
            print_level(i)
        print()

    def spiral_order(self):
        """ performs spiral order traversal on binary tree
        """
        height = self.height(self.root)

        def print_level(level, node=self.root, count=0):
            if node is not None:
                if level == count:
                    print(node.data, end=" ")
                if (level % 2 == 0):
                    print_level(level, node.right, count + 1)
                    print_level(level, node.left, count + 1)
                else:
                    print_level(level, node.left, count + 1)
                    print_level(level, node.right, count + 1)

        for i in range(height + 1):
            print_level(i)
        print()

    def left_view(self):
        """ shows left view of the tree
        """
        height = self.height(self.root)
        visited = set()

        def print_level(level, node=self.root, count=0):
            if node is not None:
                if level == count and level not in visited:
                    visited.add(level)
                    print(node.data, end=" ")
                print_level(level, node.left, count + 1)
                print_level(level, node.right, count + 1)

        for i in range(height + 1):
            print_level(i)
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

    def height(self, node, count=0):
        """ calculate the depth of a node in a binary tree
        """
        if node is not None:
            left_depth = self.height(node.left, count + 1)
            right_depth = self.height(node.right, count + 1)
            return max(left_depth, right_depth)
        else:
            return count - 1

    def depth(self, start=None):
        """ calculate the depth of a binary tree
        depth - distance from root to current node
        """

        def max_depth(node=self.root, count=0):
            if node is not None:
                left_depth = max_depth(node.left, count + 1)
                right_depth = max_depth(node.right, count + 1)
                return max(left_depth, right_depth)
            else:
                return count - 1

        def depth_current(node=self.root, count=0):
            if node is not None:
                if node is start:
                    return count
                left_count = depth_current(node.left, count + 1)
                right_count = depth_current(node.right, count + 1)
                return max(left_count, right_count)
            else:
                return 0

        if start:
            return depth_current()
        else:
            return max_depth()

    def depth2(self, start=None):
        """ calculate the depth of a binary tree, making use of
        outer variables
        """
        cmax = [0]

        def max_depth(node=self.root, count=0):
            if node is not None:
                cmax[0] = count if count > cmax[0] else cmax[0]
                max_depth(node.left, count + 1)
                max_depth(node.right, count + 1)

        def depth_current(node=self.root, count=0):
            if node is not None:
                if node is start:
                    cmax[0] = count
                depth_current(node.left, count + 1)
                depth_current(node.right, count + 1)

        if start:
            depth_current()
        else:
            max_depth()

        return cmax[0]

    def print(self):
        """ prints binary tree at 180 degrees
        """
        def printTree(node, level):
            if node is not None:
                printTree(node.right, level + 1)
                print(' ' * 4 * level + '-> ' + str(node.data))
                printTree(node.left, level + 1)
        printTree(self.root, 0)
