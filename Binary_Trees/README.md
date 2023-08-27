# Binary Trees

A binary tree is a non linear data structure. It consists of nodes, where each node as at most 2 children (left and right child node).

## Characteristics of Binary Trees:

1. **Root**: The topmost node in a binary tree is called the root node. It serves as the starting point for traversing the tree.

2. **Nodes**: Each node in a binary tree contains data and can have up to two children. The data contained within a node can be of any data type, depending on the application.

3. **Children**: A node in a binary tree can have zero, one, or two children. If a node has no children, it's called a leaf node. If it has exactly one child, it can be a left child or a right child.

4. **Parent**: A node's parent is the node from which it is descended. For any non-root node, its parent is the node from which the edge originates.

5. **Leaf Node**: A leaf node is a node that has no children. It is located at the end of a branch in the tree.

6. **Internal Node**: An internal node is a node that has at least one child. In other words, it's not a leaf node.

7. **Depth**: The depth of a node is the length of the path from the root to that node. The root node has a depth of 0. The level of a node also equates to the depth of the node.

8. **Height**: The height of a binary tree is the length of the longest path from the root to a leaf node. Alternatively, it's the maximum depth of any node in the tree.

9. **Balanced Tree**: A binary tree is considered balanced if the heights of its left and right subtrees differ by at most one for each node. Balanced trees are important for efficient search and insertion operations.

10. **Complete Tree**: A binary tree is complete if all levels, except possibly the last, are completely filled, and all nodes are as left as possible on the last level.

11. **Full Tree**: A binary tree is full if every node has either zero or two children. In other words, no node has only one child.

12. **Traversal**: Binary trees can be traversed in various ways, such as in-order (left subtree, root, right subtree), pre-order (root, left subtree, right subtree), and post-order (left subtree, right subtree, root) traversals.

13. **Binary Search Tree (BST)**: A special type of binary tree where each node's left child has a value less than its own value, and its right child has a value greater than its own value. This property allows for efficient searching, insertion, and deletion of elements.

14. **Max|Min nodes and height**:
    * max no. of nodes possible at any level 'l' is = 2^l (this node count is only for that specific level)

    <br>

    | Tree Type            | Maximum Nodes | Minimum Nodes | Maximum Height | Minimum Height  |
    |----------------------|---------------|---------------|----------------|-----------------|
    | Binary Tree          | 2^(h+1) - 1   | h + 1         | n - 1          | log2(n + 1) - 1 |
    | Full Binary Tree     | 2^(h+1) - 1   | 2h + 1        | (n-1)/2        | log2(n + 1) - 1 |
    | Complete Binary Tree | 2^(h+1) - 1   | 2^h           | logn           | log2(n + 1) - 1 |
