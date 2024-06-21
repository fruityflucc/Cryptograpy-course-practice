def s_box(input_6bit):
    s_box_table = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 6, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ]
    input_decimal = int(input_6bit, 2)
    row = (input_decimal & 0b100000) >> 4 | (input_decimal & 0b1)
    col = (input_decimal & 0b011110) >> 1
    output_decimal = s_box_table[row][col]
    output_4bit = format(output_decimal, '04b')
    return output_4bit


input_bits = "101010"
output_bits = s_box(input_bits)
print(f"Input: {input_bits}, Output: {output_bits}")