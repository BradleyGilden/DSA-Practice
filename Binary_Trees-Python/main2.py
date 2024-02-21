#!/usr/bin/env python3

"""
This file is for testing binary search tree's

Author: Bradley Dillion Gilden
Date: 21-02-2024
"""
from bst import BST  # noqa


if __name__ == '__main__':
    bst = BST()

    bst.construct_from_preorder([8, 5, 1, 7, 10, 12])
    bst.print()

    bst.construct_preorder_n_inorder([10, 20, 40, 50, 30, 60],
                                     [40, 20, 50, 10, 60, 30])
    bst.print()
