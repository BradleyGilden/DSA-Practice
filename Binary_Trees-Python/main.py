#!/usr/bin/env python3

"""
This file is for testing the Binary Tree structure

Author: Bradley Dillion Gilden
Date: 15-02-2024
"""
from binary_tree import BinaryTree, Node


if __name__ == '__main__':
    bt = BinaryTree(1)
    bt.root.left = Node(32, Node(24, Node(9), Node(3)), Node(2))
    bt.root.right = Node(11, Node(39), Node(74))

    bt.print()
    print("\nPre-Order Traversal")
    bt.pre_order()
    print("\nIn-Order Traversal")
    bt.in_order()
    print("\nPost-Order Traversal")
    bt.post_order()
    print("\nNumber of Nodes")
    print(bt.count())
