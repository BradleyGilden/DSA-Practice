"""
DEPTH FIRST SEARCH (using Graph 2 from the README)
"""
from custom_structs import Stack, Queue  # noqa


def hasPath(graph: dict, start: str, end: str):
    # init stack
    if (start == end):
        return True
    for neighbour in graph[start]:
        if hasPath(graph, neighbour, end):
            return True

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
