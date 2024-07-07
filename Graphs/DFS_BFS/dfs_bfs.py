"""
DEPTH FIRST SEARCH (using Graph 1 from the README)
"""
from custom_structs import Stack, Queue  # noqa


def depthFirstSearch(graph: dict, start: str):
    # init stack
    stack = Stack(start)

    while (len(stack)):
        current = stack.pop()
        print(current)
        # add neigbours to stack (adjacent nodes)
        for neighbour in graph[current]:
            stack.push(neighbour)


def depthFirstSearch_v2(graph: dict, start: str):
    # dfs with recursion
    print(start)
    for node in graph[start]:
        depthFirstSearch_v2(graph, node)


def breadthFirstSearch(graph, start):
    queue = Queue(start)

    while (len(queue)):
        current = queue.dequeue()
        print(current)
        for neighbour in graph[current]:
            queue.enqueue(neighbour)


if __name__ == '__main__':
    graph = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }
    print("DFS w/ loops\n")
    depthFirstSearch(graph, 'a')
    print("\nDFS w/ recursion\n")
    depthFirstSearch_v2(graph, 'a')
    print("\nBFS w/ loops\n")
    breadthFirstSearch(graph, 'a')
