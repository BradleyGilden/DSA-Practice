"""
Find smallest island (using Graph 6 from the README)
"""

from typing import List, Tuple


def get_neighbours(numRows, numCols, location: Tuple[int]) -> List[Tuple[int]]:
    """creates a list of neighbour co-ordinates"""

    neighbours = []

    if location[0] - 1 > -1:
        neighbours.append((location[0] - 1, location[1]))
    if location[0] + 1 < numRows:
        neighbours.append((location[0] + 1, location[1]))
    if location[1] - 1 > -1:
        neighbours.append((location[0], location[1] - 1))
    if location[1] + 1 < numCols:
        neighbours.append((location[0], location[1] + 1))

    return neighbours


def smallest_island(graph):
    """find smallest island"""

    visited = set()
    numRows = len(graph)
    numCols = len(graph[0])

    def island_size(current):
        nodeVal = graph[current[0]][current[1]]
        if nodeVal == "W" or current in visited:
            return 0
        visited.add(current)
        counter = 1

        neighbours = get_neighbours(numRows, numCols, current)

        for node in neighbours:
            counter += island_size(node)

        return counter

    smallest = numRows * numCols + 1
    for r in range(numRows):
        for c in range(numCols):
            size = island_size((r, c))
            if size:
                smallest = size if size < smallest else smallest

    return smallest if smallest < numRows * numCols + 1 else - 1


if __name__ == "__main__":
    graph = [
        ["W", "L", "W", "W", "L", "W"],
        ["L", "L", "W", "W", "L", "W"],
        ["W", "L", "W", "W", "W", "W"],
        ["W", "W", "W", "L", "L", "W"],
        ["W", "W", "W", "L", "L", "W"],
        ["W", "W", "W", "L", "W", "W"],
    ]

    print(smallest_island(graph))
