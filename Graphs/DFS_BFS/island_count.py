"""
count number of islands (using Graph 6 from the README)
"""
from typing import List, Tuple


def get_neighbours(numRows, numCols, index: Tuple[int]) -> List[Tuple[int]]:
    """creates a list of neighbour co-ordinates"""

    neighbours = []

    if (index[0] - 1 > -1):
        neighbours.append((index[0] - 1, index[1]))
    if (index[0] + 1 < numRows):
        neighbours.append((index[0] + 1, index[1]))
    if (index[1] - 1 > -1):
        neighbours.append((index[0], index[1] - 1))
    if (index[1] + 1 < numCols):
        neighbours.append((index[0], index[1] + 1))

    return neighbours


def count_islands(graph: List[List[int]]) -> bool:
    visitedLand = set()
    counter = 0
    numRows = len(graph)
    numCols = len(graph[0])

    def is_island(current: Tuple[int]):
        nodeVal = graph[current[0]][current[1]]
        if nodeVal == 'W' or current in visitedLand:
            return False
        visitedLand.add((current))
        neighbours = get_neighbours(numRows, numCols, current)
        for node in neighbours:
            is_island(node)

        return True

    for r in range(numRows):
        for c in range(numCols):
            if is_island((r, c)):
                counter += 1

    return counter


if __name__ == '__main__':
    graph = [
        ['W', 'L', 'W', 'W', 'L', 'W'],
        ['L', 'L', 'W', 'W', 'L', 'W'],
        ['W', 'L', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'L', 'W'],
        ['W', 'L', 'W', 'L', 'L', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'W']
    ]

    print(count_islands(graph))
