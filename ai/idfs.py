from util import actions
from util import get_element_value_by_direction
from sys import maxsize

def depth_limited_search(start: tuple, end: tuple, matrix: list):
    result = []
    for i in range(1, maxsize):
        res = recursive_dls(start, end, matrix, i, result)
        if res is not None and res != "cutoff" and res != "failure":
            result.insert(0, start)
            return result
        else:
            result = []


def recursive_dls(start: tuple, end: tuple , matrix: list, limit: int, result: list):
    if start is None:
        return "failure"
    if start == end:
        return [start]
    elif limit == 0:
        return None
    else:
        cutoff_occurred = False
    for action in actions:
        child = get_element_value_by_direction(matrix, start[0], start[1],
                                               action, matrix[start[0]][start[1]])

        res = recursive_dls(child, end, matrix, limit - 1, result)
        if res == "cutoff":
            cutoff_occurred = True
        elif res is not None and res != "failure":
            result.insert(0, child)
            return res
    if cutoff_occurred:
        return "cutoff"
    else:
        return "failure"


def jumpsolve_ids(start: tuple, end: tuple, matrix: list):
    return depth_limited_search(start, end, matrix)


if __name__ == "__main__":
    print(jumpsolve_ids((0, 0), (2, 2), [[2, 1, 0], [0, 1, 1], [1, 2, 1]]))