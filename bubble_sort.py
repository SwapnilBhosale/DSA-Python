def bubble_sort(arr: list):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


assert(bubble_sort([4, 1, 3, 2]) == [1, 2, 3, 4])
assert(bubble_sort([8, 1, 2, 5, 4, 7, 6, 3]) == [1, 2, 3, 4, 5, 6, 7, 8])