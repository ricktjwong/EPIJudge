from test_framework import generic_test


def swap_bits(x, i, j):
    binary = bin(x)
    if binary[2 + i] == binary[2 + j]:
        return x
    new = binary[0:2+i] + binary[2+j] + binary[2+i+1:2+j] + binary[2+i] + binary[2+j+1:]
    print(x)
    return int(new, 2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("swap_bits.py", 'swap_bits.tsv',
                                       swap_bits))
