from util import actions
from util import get_element_value_by_direction


class Node:
    def __init__(self, point, val):
        self.point = point
        self.val = val
        self.g = 0
        self.parent = None
        self.h = 0


def calculate_manhattan_heuristics(current, goal):
    return abs(current.point[0] - goal.point[0]) - abs(current.point[1] - goal.point[1])


def astar(start, goal, grid):
    n = len(grid)
    open_set = set()
    close_set = set()

    open_set.add(start)
    while open_set:
        current = min(open_set, key=lambda o: o.g + o.h)
        if current.point == goal.point:
            path = []
            while current.parent:
                path.append(current.point)
                current = current.parent
            path.append(current.point)
            return path[::-1]
        open_set.remove(current)
        close_set.add(current)
        r, c = current.point
        jump_size = current.val
        neighbours = []
        for action in actions:
            if action == "left" and c - jump_size >= 0:
                neighbours.append(grid[r][c - jump_size])
            elif action == "right" and c + jump_size < n:
                neighbours.append(grid[r][c + jump_size])
            elif action == "up" and r - jump_size >= 0:
                neighbours.append(grid[r - jump_size][c])
            elif action == "down" and r + jump_size < n:
                neighbours.append(grid[r + jump_size][c])

        #iterate through all the neighbours
        for node in neighbours:
            #if it's already in the close set then continue
            if node in close_set:
                continue
            #if is is already in open set
            if node in open_set:
                updated_g = current.g + current.val
                if node.g > updated_g:
                    node.g = updated_g
                    node.parent = current
            else:
                node.g = current.g + current.val
                node.h = calculate_manhattan_heuristics(node, goal)
                node.parent = current
                open_set.add(node)


def jumpsolve_astar(start: tuple, end: tuple, matrix: list):
    n = len(matrix)
    for row in range(n):
        for col in range(n):
            matrix[row][col] = Node((row, col), matrix[row][col])
    s_r, s_c = start
    g_r, g_c = end
    return astar(matrix[s_r][s_c], matrix[g_r][g_c], matrix)


if __name__ == "__main__":
    print(jumpsolve_astar((0, 0), (2, 2), [[2, 1, 0], [0, 1, 1], [1, 2, 1]]))