def insertion_sort(a: list):
    for i in range(len(a)):
        temp = a[i]
        j = i
        while j > 0 and temp < a[j-1]:
            a[j] = a[j-1]
            j -= 1
        a[j] = temp
    return a


assert(insertion_sort([5, 1, 3, 2, 4]) == [1, 2, 3, 4,5])
