'''
    Find non repeating 2 numbers from the given array :
    Solution :
    1) Take XOR of all elements. The bits will be set in the result will be from the on repeating numbers
        Since XOR of two same number is zero
    2) Find right most set bit
    3) For all elements in array. Create two list
        a) AND right_most_set_bit with arr[i] if ans is 1. XOR the element with first list
        b) else XOR the element with second list
    4) The first and second would be non-repeating numbers

Reference : https://www.geeksforgeeks.org/find-two-non-repeating-elements-in-an-array-of-repeating-elements/

'''


def find_non_repeating_numbers(arr: list):
    xor = arr[0]

    for i in range(1, len(arr)):
        xor ^= arr[i]

    rightmost_set_bit = xor & ~(xor - 1)
    first = 0
    second = 0
    for i in arr:
        if i & rightmost_set_bit:
            first ^= i
        else:
            second ^= i

    return first, second


assert(find_non_repeating_numbers([1, 4, 7, 7, 1, 8, 4, 9]) == (9, 8))
assert (find_non_repeating_numbers([2, 3, 7, 9, 11, 2, 3, 11]) == (7, 9))