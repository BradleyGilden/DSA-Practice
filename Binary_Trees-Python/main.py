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
    print("\nTree 1")
    bt.print()
    print("\nPre-Order Traversal")
    bt.pre_order()
    print("\nIn-Order Traversal")
    bt.in_order()
    print("\nPost-Order Traversal")
    bt.post_order()
    print("\nLevel-Order Traversal")
    bt.level_order()
    print("\nReversed Level-Order Traversal")
    bt.rlevel_order()
    print("\nSpiral Order traversal")
    bt.spiral_order()
    print("\nNumber of Nodes")
    print(bt.count())
    print("\nmax depth | max height")
    print(bt.depth())
    print("\ndepth from 24")
    print(bt.depth(bt.root.left.left))
    print("\nheight from 32")
    print(bt.height(bt.root.left))
    print("\nis complete?")
    print(bt.is_complete())

    bt2 = BinaryTree(1)
    bt2.root.right = Node(32, right=Node(24, right=Node(9)), left=Node(2))
    bt2.root.left = Node(11, Node(39), Node(74))

    print("\nTree 2")
    bt2.print()
    print("\nLeft view")
    bt2.left_view()
    print("\nBottom view")
    bt2.bottom_view()

    print("\nNext node after 11")
    node = bt2.next_node_same_level(bt2.root.left)
    print(node.data if node else None)
    print("\nNext node after 24")
    node = bt2.next_node_same_level(bt2.root.right.right)
    print(node.data if node else None)
    print("\nis complete?")
    print(bt2.is_complete())

    bt3 = BinaryTree(1)
    bt3.root.right = Node(3)
    bt3.root.left = Node(2, right=Node(4, right=Node(5, right=Node(6))))
    print("""\nTree 3
            1
           / \\
          2   3
           \\
            4
             \\
              5
               \\
                6
""")
    print("\nRight view")
    bt3.right_view()
    print("\nBottom view")
    bt3.bottom_view()
    print("\nTop view")
    bt3.top_view()
    print("\nis complete?")
    print(bt3.is_complete())
