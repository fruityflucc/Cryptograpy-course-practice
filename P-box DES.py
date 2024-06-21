def p_box(input_bits):
    permutation_table = [
        16, 7, 20, 21, 29, 12, 28, 17,
        1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9,
        19, 13, 30, 6, 22, 11, 4, 25
    ]
    output_bits = [input_bits[i - 1] for i in permutation_table]
    return output_bits


input_bits = [
    1, 0, 1, 0, 0, 1, 0, 1,
    0, 1, 0, 1, 1, 0, 0, 1,
    1, 1, 0, 0, 0, 1, 1, 0,
    0, 0, 1, 1, 1, 1, 0, 0
]
output_bits = p_box(input_bits)
print("Input Bits:", input_bits)
print("Output Bits after P-box Permutation:", output_bits)