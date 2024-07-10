"""
shortest path (using Graph 6 from the README)
We use BFS since paths are explored evenly
"""


from custom_structs import Queue


def buildGraph(edge_list) -> dict:
    """builds a graph from an edge_list"""
    edge_list_flat = set([j for i in edge_list for j in i])
    graph = {k: [] for k in edge_list_flat}
    for row in edge_list:
        graph[row[0]].append(row[1])
        graph[row[1]].append(row[0])

    return graph


def shortestPath(edges, start, end):
    """find the shorted path between 2 nodes in a graph"""
    graph = buildGraph(edges)
    visited = set()
    queue = Queue([[start, 0]])

    while (len(queue)):
        current, distance = queue.dequeue()
        visited.add(current)
        for node in graph[current]:
            if node not in visited:
                if node == end:
                    return distance + 1
                queue.enqueue([node, distance + 1])

    return -1  # no path found


if __name__ == '__main__':
    edge_list = [
        ['w', 'x'],
        ['w', 'v'],
        ['v', 'z'],
        ['z', 'y'],
        ['y', 'x']
    ]

    print(shortestPath(edge_list, 'w', 'z'))
