'''
    Python program to demonstrate the number of bit flips required to change A to B
    Algorithm :
        1) calculate A XOR B
        2) Find the number of 1's in the above result.
    Example : 10 , 20
        Binary representation of 10 is 01010
        Binary representation of 20 is 10100

        01010
    xor 10100
    ------------
        11110
    Thus for above problem 4 bit flips will be required.

    How do you calculate number of set bits ?
    1) initialize count while "num" is greater than 0
        a) AND the "num" with 1. Which will return 1 if LSB is 1
        b) increment count if above result is 1
        c) right shift num by 1

     check the count_set_bits() function below
'''

def flip_bits(a: int , b: int):
    res = a ^ b
    return count_set_bits(res)


def count_set_bits(num: int):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count


assert (flip_bits(10, 20) == 4)
assert (flip_bits(7, 10) == 3)
assert (flip_bits(2, 1) == 2)