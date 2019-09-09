count = -1


def binary_search_recursive(a: list, l: int, h: int, key: int):
    if l > h:
        return -1
    m = (l + h) // 2
    if a[m] == key:
        return m
    if a[m] > key:
        h = m - 1
    else:
        l = m + 1
    return binary_search_recursive(a, l, h, key)


def binary_search_non_recursive(a: list, l: int, h: int, key: int):
    while l <= h:
        m = (l + h) // 2
        if a[m] == key:
            return m
        if a[m] > key:
            h = m - 1
        else:
            l = m + 1
    return -1


def binary_search(a: list, key: int):
    global count
    count += 1
    if count // 2 == 0:
        return binary_search_recursive(a, 0, len(a) - 1, key)
    else:
        return binary_search_non_recursive(a, 0, len(a) - 1, key)


assert(binary_search([1, 2, 3, 4, 5, 6], 8) == -1)
assert(binary_search([1, 2, 3, 4, 5, 6], 1) == 0)
assert(binary_search([1, 2, 3, 4, 5, 6], 3) == 2)
assert(binary_search([1, 2, 3, 4, 5, 6], 6) == 5)
assert(binary_search([1, 2, 3, 4, 5, 6], 7) == -1)
assert(binary_search([1, 2, 3, 4, 5, 6], 1) == 0)
assert(binary_search([1, 2, 3, 4, 5, 6], 9) == -1)
assert(binary_search([1, 2, 3, 4, 5, 6], 10) == -1)