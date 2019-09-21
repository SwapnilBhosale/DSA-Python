from util import actions
from util import get_element_value_by_direction
from queue import Queue

def jumpsolve_bfs(start: tuple, end: tuple, matrix: list):
    if start == end:
        return [start]
    result = []
    frontier = Queue()
    explored = set()
    frontier.put(start)
    while True:
        if frontier.empty():
            return None
        curr_node = frontier.get()
        result.append(curr_node)
        explored.add(curr_node)
        for action in actions:
            child = get_element_value_by_direction(matrix, curr_node[0], curr_node[1],
                                                   action, matrix[curr_node[0]][curr_node[1]])
            if child is not None and not (child in explored or child in frontier.queue):
                if child == end:
                    result.append(child)
                    return result
                elif matrix[child[0]][child[1]] is not 0:
                    frontier.put(child)


if __name__ == "__main__":
    print(jumpsolve_bfs((0, 0), (2, 2), [[2, 1, 0], [0, 1, 1], [1, 2, 1]]))