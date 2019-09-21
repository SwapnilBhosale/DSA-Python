actions = ["left", "up", "right", "down"]

def get_element_value_by_direction(arr, row, col, action, jump_size):
    val = None
    if action == "left" and col - jump_size >= 0:
        val = (row, col - jump_size)
    elif action == "right" and col + jump_size < len(arr):
        val = (row, col + jump_size)
    elif action == "up" and row - jump_size >= 0:
        val = (row - jump_size, col)
    elif action == "down" and row + jump_size < len(arr):
        val = (row + jump_size, col)
    return val