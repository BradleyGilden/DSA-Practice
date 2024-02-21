#!/usr/bin/env python3

"""
Contains binary search tree class that inherits from binary tree

Author: Bradley Dillion Gilden
Date: 21-02-2024
"""
from binary_tree import BinaryTree, Node  # noqa
from sys import maxsize as maxint


class BST(BinaryTree):
    """ this class represents a binary search tree
    """
    def __init__(self):
        super().__init__()

    def construct_from_preorder(self, arr):
        """ constructs a binary search tree from a pre-order list
        """
        i = [0]

        def construction(bound):
            if (i[0] == len(arr) or arr[i[0]] > bound):
                return None
            root = Node(arr[i[0]])
            i[0] += 1
            root.left = construction(root.data)
            root.right = construction(bound)
            return root

        self.root = construction(maxint)

    def construct_preorder_n_inorder(self, preorder, inorder):
        """ construct from preorder and in order list
        """
        hashin = {inorder[i]: i for i in range(len(inorder))}
        i = [0]

        def construction(preord, inord):
            if (i[0] == len(inorder) or not inord):
                return None
            root = Node(preorder[i[0]])
            rootidx = hashin[root.data] - 1 if hashin[root.data] > 0 else 0
            l_inorder = inord[rootidx::-1]
            rootidx = hashin[root.data] + 1
            r_inorder = inord[rootidx:]
            i[0] += 1
            root.left = construction(preord[:len(l_inorder) + 1], l_inorder)
            root.right = construction(preord[len(l_inorder) + 1:], r_inorder)
            return root

        self.root = construction(preorder, inorder)
