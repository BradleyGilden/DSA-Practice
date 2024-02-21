#!/usr/bin/python3

"""
This module contains the binary tree class for setting up binary trees

Author: Bradley Dillion Gilden
Date: 22-10-2023
"""
from math import pow


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
        visited_levels = set()

        # use level traversal starting from the left side, only print one node
        # per level
        def print_level(level, node=self.root, count=0):
            if node is not None:
                if level == count and level not in visited_levels:
                    visited_levels.add(level)
                    print(node.data, end=" ")
                print_level(level, node.left, count + 1)
                print_level(level, node.right, count + 1)

        for i in range(height + 1):
            print_level(i)
        print()

    def right_view(self):
        """ displays right view of binary tree
        """
        height = self.height(self.root)
        visited_levels = set()

        # use level traversal starting from the right side, only print one node
        # per level
        def print_level(level, node=self.root, count=0):
            if (node is not None):
                if (count == level and level not in visited_levels):
                    visited_levels.add(level)
                    print(node.data, end=" ")
                print_level(level, node.right, count + 1)
                print_level(level, node.left, count + 1)

        for i in range(height + 1):
            print_level(i)

        print()

    def bottom_view(self):
        """ display bottom view of a binary tree
        """
        height = self.height(self.root)
        visited_shifts = set()
        b_view = {}

        # the shift will tell us if a horizontal position was visited
        # we use reverse level traversal, although in the same direction
        # just starting from the bottom
        def rlevel_traversal(level, node=self.root, count=0, shift=0):
            if (node is not None):
                if (level == count and shift not in visited_shifts):
                    visited_shifts.add(shift)
                    b_view[shift] = node.data
                rlevel_traversal(level, node.left, count + 1, shift - 1)
                rlevel_traversal(level, node.right, count + 1, shift + 1)

        for i in range(height, -1, -1):
            rlevel_traversal(i)
        # ensure keys are sorted according to shifts when printed
        for key in sorted(b_view.keys()):
            print(b_view[key], end=" ")
        print()

    def top_view(self):
        """ display bottom view of a binary tree
        """
        height = self.height(self.root)
        visited_shifts = set()
        b_view = {}

        # the shift will tell us if a horizontal position was visited
        # we use reverse level traversal, although in the same direction
        # just starting from the bottom
        def level_traversal(level, node=self.root, count=0, shift=0):
            if (node is not None):
                if (level == count and shift not in visited_shifts):
                    visited_shifts.add(shift)
                    b_view[shift] = node.data
                level_traversal(level, node.left, count + 1, shift - 1)
                level_traversal(level, node.right, count + 1, shift + 1)

        for i in range(height + 1):
            level_traversal(i)
        # ensure keys are sorted according to shifts when printed
        for key in sorted(b_view.keys()):
            print(b_view[key], end=" ")
        print()

    def next_node_same_level(self, node):
        """ find the next node in the same level
        """
        if (node is None):
            return None

        # get the level and shift position of node given
        def get_level_n_shift(n1=self.root, n2=node, count=0, shift=0):
            if (n1 is not None):
                if (n1 is n2):
                    return [count, shift]
                l_count, l_shift = get_level_n_shift(n1.left, n2,
                                                     count + 1, shift - 1)
                r_count, r_shift = get_level_n_shift(n1.right, n2,
                                                     count + 1, shift + 1)

                return ([l_count, l_shift]
                        if l_count > r_count else [r_count, r_shift])
            else:
                return [0, 0]

        level, shift = get_level_n_shift()

        # track the shift that was used
        used_shift = [None]
        # return the node that is a shift higher on the same level
        def get_next_node(node=self.root, level=level, count=0,
                          s1=shift, s2=0):
            if (node is not None):
                if (count == level and s2 > s1 and s2 != used_shift[0]):
                    used_shift[0] = s2
                    return node
                l_node = get_next_node(node.left, level,
                                       count + 1, s1, s2 - 1)
                r_node = get_next_node(node.right, level,
                                       count + 1, s1, s2 + 1)
                return l_node if l_node is not None else r_node
            else:
                return None

        return get_next_node()

    def is_complete(self):
        """checks if a biary tree is complete"""
        height = self.height(self.root)
        count = self.count()

        # check if they have the minimum number of nodes to satisfy a
        # complete binary tree
        if count < pow(2, height):
            return False

        def check_end_nodes(level=height-1, node=self.root, count=0):
            if node is not None:
                if (count == level):
                    if (node.left is None and node.right):
                        return False
                rtree = check_end_nodes(level, node.right, count + 1)
                ltree = check_end_nodes(level, node.left, count + 1)
                return ltree & rtree
            else:
                return True

        return check_end_nodes()

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
