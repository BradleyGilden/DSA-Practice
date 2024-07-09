"""
count connected components (using Graph 4 from the README)
"""


def countConnComponents(graph):
    """counts components present in graph using DFS"""
    visited = set()
    count = 0

    def verifyConnection(current):
        """verifies one connected component by completing a dfs iteration"""
        if current in visited:
            return False

        visited.add(current)

        for node in graph[current]:
            verifyConnection(node)

        return True

    for node in graph.keys():
        if verifyConnection(node):
            count += 1

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
