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
| Binary Tree          | $CEIL[\log_2{(n + 1)}] - 1$ | $n - 1$          |
| Full Binary Tree     | $CEIL[\log_2{(n + 1)}] - 1$ | $\dfrac{n-1}{2}$ |
| Complete Binary Tree | $CEIL[\log_2{(n + 1)}] - 1$ | $\log_2{n}$      |
