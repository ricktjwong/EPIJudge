from test_framework import generic_test


def count_bits(x: int) -> int:
    # TODO - you fill in here.
    num_bits = 0
    while x:
        # Takes least significant bit, AND with 1
        num_bits += x & 1
        # Bit shift right by one, e.g. 0101 -> 010
        x >>= 1
    return num_bits


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("count_bits.py", 'count_bits.tsv',
                                       count_bits))
