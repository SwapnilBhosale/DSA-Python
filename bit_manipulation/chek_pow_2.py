'''
    Check whether given number is power of 2.
    The logic is , if we AND the power of 2 number with the number one less that that,
    the output will be zero

    example: We are checking if 8 is power of 2
     8 -> 1000
     7 -> 0111

    8 & 7 = 1 0 0 0
            0 1 1 1
           ---------
            0 0 0 0
'''

def check_power_two(num: int):
    if num == 0:
        return 0
    if num & (num - 1) == 0:
        return 1
    return -1


output = {
    1: "Number {} is power of two",
    0: "Number is zero",
    -1: "Number {} is not power of two"
}


assert (output[check_power_two(2)].format(2) == "Number 2 is power of two")
assert (output[check_power_two(6)].format(6) == "Number 6 is not power of two")
assert (output[check_power_two(0)] == "Number is zero")
assert (output[check_power_two(128)].format(128) == "Number 128 is power of two")
assert (output[check_power_two(15-15)].format(2) == "Number is zero")