def partition(a:list, l: int, h: int):
    # we are taking always pivot as last element in the array
    pivot = a[h]
    i = l - 1
    for j in range(l, h):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[h] = a[h], a[i+1]
    return i+1


def quick_sort(a: list, l: int, h: int):
    if l < h:
        #get the pivot element
        pivot = partition(a, l, h)
        #recurse first half till pivot
        quick_sort(a, l, pivot - 1)
        #recurse second half after pivot
        quick_sort(a, pivot + 1, h)
    return a

assert(quick_sort([5, 3, 1, 2, 4, 6, 0], 0, 6) == [0, 1, 2, 3, 4, 5, 6])
assert(quick_sort([5, 3, 1, 2, 4], 0, 4) == [1, 2, 3, 4, 5])