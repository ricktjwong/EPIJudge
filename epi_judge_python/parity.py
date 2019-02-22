from test_framework import generic_test


def parity_O_n(x):
    """
    e.g. 
    1. x = 101
    result = 0. result ^= 1 & 1 = 1
    2. x = 10
    result = 1. result ^= 0 & 1 = 1
    3. x = 1
    result = 1. result ^= 1 & 1 = 0

    Time complexity is O(n), where n is the
    word size.
    """
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


def parity_O_k(x):
    """
    e.g. 
    1. x = 101
    result = 0. result ^= 1 = 1.
    2. x = 1
    result ^= 1 = 0

    Just check the 1's. Result will alternate
    between 0 and 1 as it counts the number of
    1's present.

    Time complexity is O(k), where k is the
    number of 1's.
    """
    result = 0
    while x:
        # XOR with 1
        result ^= 1
        # Drop the lowest set bit of x
        x &= x - 1
    return result

def parity_O_log_n(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity_O_log_n))
