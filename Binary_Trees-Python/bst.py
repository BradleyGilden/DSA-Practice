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
        """ construct a binary tree from preorder and in order list
        """
        # create hash of inorder elments as keys and indexes as values
        inhash = {inorder[i]: i for i in range(len(inorder))}
        prelen = len(preorder) - 1
        inlen = len(inorder) - 1

        def construction(prestart, pre_end, instart, in_end):
            if (prestart > pre_end or instart > in_end):
                return None
            root = Node(preorder[prestart])
            # get root index
            rootidx = inhash[root.data]
            # get number of elements to the left
            print(rootidx, root.data)
            nums_left = rootidx - instart
            root.left = construction(prestart + 1, prestart + nums_left,
                                     instart, rootidx - 1)
            root.right = construction(prestart + nums_left + 1, pre_end,
                                      rootidx + 1, in_end)
            return root

        self.root = construction(0, prelen, 0, inlen)
