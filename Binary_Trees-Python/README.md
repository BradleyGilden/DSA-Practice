# Binary Trees - Python

This directory contains practicing manipulating binary tree data structures in python<br>

The basic binary tree datastructure being used:

```Python
class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data
```

|                      | Max nodes                   | Min nodes        |
|----------------------|:---------------------------:|:----------------:|
| Binary Tree          | $2^{h+1}$                   | $h + 1$          |
| Full Binary Tree     | $2^{h+1}$                   | $2h + 1$         |
| Complete Binary Tree | $2^{h+1}$                   | $2^h$            |

|                      | Min Height                  | Max Height       |
|----------------------|:---------------------------:|:----------------:|
| Binary Tree          | $CEIL[\log_2{(n - 1)}] - 1$ | $n - 1$          |
| Full Binary Tree     | $CEIL[\log_2{(n - 1)}] - 1$ | $\dfrac{n-1}{2}$ |
| Complete Binary Tree | $CEIL[\log_2{(n - 1)}] - 1$ | $\log_2{n}$      |

## Array Reperesentation (complete binary trees)

```
                     A
                    / \
                   B   C
                  / \
                 D   E
 0  1  2  3  4
[A][B][C][D][E]

 1  2  3  4  5
[A][B][C][D][E]
```

left child = $(2\cdot{i}) + 1$ <br>
right child = $(2\cdot{i}) + 2$ <br>
parent = $FLOOR[\dfrac{i - 1}{2}]$

where $i$ is the position of the current node starting from 0

left child = $(2\cdot{i})$ <br>
right child = $(2\cdot{i}) + 1$ <br>
parent = $FLOOR[\dfrac{i}{2}]$

where $i$ is the position of the current node starting from 1
