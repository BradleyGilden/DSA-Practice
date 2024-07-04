"""
DFS - Depth First Search Algorithm

see dfs.md for diagrams
"""


from typing import List


def depth_first_search(graph: List[List[int]], adj_list):
    """prints nodes using dfs"""
    n = len(graph)
    visited = [False for _ in range(n)]
    start = 0

    def dfs(at):
        if visited[at]:
            print(f"     x-{at}-x")
            return
        print(at, '--->', end="")
        visited[at] = True
        neighbours = adj_list[at]
        for node in neighbours:
            dfs(node)

    dfs(start)


if __name__ == '__main__':
    adj_list = [
        [1, 9],
        [0, 8],
        [3],
        [2, 4, 5, 7],
        [3],
        [3, 6],
        [5, 7],
        [3, 6, 10, 11],
        [1, 7, 9],
        [0, 8],
        [7, 11],
        [7, 10]
    ]

    graph = [i for i in range(12)]

    depth_first_search(graph, adj_list)
