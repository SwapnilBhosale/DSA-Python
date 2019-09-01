def merge(a: list, left: list, right: list):
    i, j, k = 0 , 0, 0
    length_left = len(left)
    length_right = len(right)
    while i < length_left and j < length_right:
        if left[i] < right[j]:
            a[k] = left[i]
            k += 1
            i += 1
        else:
            a[k] = right[j]
            k += 1
            j += 1
    while i < length_left:
        a[k] = left[i]
        k += 1
        i += 1
    while j < length_right:
        a[k] = right[j]
        k += 1
        j += 1


def merge_sort(a: list):
    length = len(a)
    if length > 1:
        mid = length // 2
        left = a[:mid]
        right = a[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(a, left, right)
    return a

assert(merge_sort([5, 3, 2, 1, 4]) == [1, 2, 3, 4, 5])