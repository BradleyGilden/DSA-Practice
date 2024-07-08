"""
Find if path (undirected) exists (using Graph 3 from the README)
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


def undirectedPath(edges, src, dst, dfs=True):
    graph = buildGraph(edges)
    visited = set()

    def hasPathDFS(current):
        if (current in visited):
            return
        # visited node
        visited.add(current)
        if current == dst:
            return True

        for node in graph[current]:
            if hasPathDFS(node):
                return True

        return False

    def hasPathBFS(src):
        queue = Queue(src)
        visited = set()

        while (len(queue)):
            current = queue.dequeue()
            visited.add(current)
            if current == dst:
                return True
            for node in graph[current]:
                if node not in visited:
                    queue.enqueue(node)

        return False

    return hasPathDFS(src) if dfs else hasPathBFS(src)


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
    print()
    print(undirectedPath(edge_list, 'i', 'm', False))
    print(undirectedPath(edge_list, 'k', 'o', False))
    print(undirectedPath(edge_list, 'n', 'o', False))
