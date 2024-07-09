"""
count connected components (using Graph 4 from the README)
"""


def countConnComponents(graph):
    """counts nodes present in graph using DFS"""

    return count


if __name__ == '__main__':
    graph = {
        3: [],
        4: [6],
        5: [6],
        6: [4, 5, 7, 8],
        8: [6],
        7: [6],
        1: [2],
        2: [1]
    }

    print(countConnComponents(graph))
