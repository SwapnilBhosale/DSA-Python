def selection_sort(a):
    for i in range(len(a)):
        min_i = i
        for j in range(i+1, len(a)):
            if a[min_i] > a[j]:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]
    return a


assert(selection_sort([1, 3, 2, 5, 4]) == [1, 2, 3, 4, 5])
assert(selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5])