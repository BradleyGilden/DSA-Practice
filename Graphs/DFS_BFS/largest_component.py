"""
find largest component (using Graph 5 from the README)
"""


def largestComponent(graph):
    """counts nodes present in graph using DFS"""
    visited = set()

    def countNodes(current):
        if current in visited:
            return 0

        visited.add(current)
        counter = 1
        for node in graph[current]:
            counter += countNodes(node)

        return counter

    largest = 0
    for node in graph.keys():
        componentSize = countNodes(node)
        largest = componentSize if componentSize > largest else largest
    return largest


if __name__ == '__main__':
    graph = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }

    print(largestComponent(graph))
