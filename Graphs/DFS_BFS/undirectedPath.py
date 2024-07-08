"""
Find if path (undirected) exists (using Graph 3 from the README)
"""


def buildGraph(edge_list) -> dict:
    """builds a graph from an edge_list"""
    edge_list_flat = set([j for i in edge_list for j in i])
    graph = {k: [] for k in edge_list_flat}
    for row in edge_list:
        graph[row[0]].append(row[1])
        graph[row[1]].append(row[0])

    return graph


def undirectedPath(edges, src, dst):
    graph = buildGraph(edges)
    visited = set()

    def hasPath(current):
        if (current in visited):
            return
        # visited node
        visited.add(current)
        if current == dst:
            return True

        for node in graph[current]:
            if hasPath(node):
                return True

        return False

    return hasPath(src)


if __name__ == '__main__':
    edge_list = [
        ['i', 'j'],
        ['j', 'k'],
        ['k', 'i'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'n']
    ]

    print(undirectedPath(edge_list, 'i', 'm'))
    print(undirectedPath(edge_list, 'k', 'o'))
    print(undirectedPath(edge_list, 'n', 'o'))
