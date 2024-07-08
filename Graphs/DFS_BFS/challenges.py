"""
DEPTH FIRST SEARCH (using Graph 2 from the README)
"""
from custom_structs import Stack, Queue  # noqa


def hasPath(graph: dict, start: str, end: str):
    """ Depth First Version
    """
    if (start == end):
        return True
    for neighbour in graph[start]:
        if hasPath(graph, neighbour, end):
            return True

    return False


def hasPath_v2(graph: dict, start: str, end: str):
    """ Breadth First Version
    """
    # init queue
    queue = Queue(start)

    while (len(queue)):
        current = queue.dequeue()
        if (current == end):
            return True
        for neighbour in graph[current]:
            queue.enqueue(neighbour)

    return False


if __name__ == '__main__':
    graph = {
        'f': ['g', 'i'],
        'i': ['k', 'g'],
        'g': ['h'],
        'j': ['i'],
        'h': [],
        'k': []
    }
    print(hasPath(graph, 'k', 'f'))
    print(hasPath(graph, 'i', 'g'))
    print(hasPath_v2(graph, 'k', 'f'))
    print(hasPath_v2(graph, 'f', 'k'))
