def process_input_text(original_text):
    modified_text = original_text.upper().replace('J', 'I')
    modified_text = ''.join(filter(str.isalpha, modified_text))
    digraphs = [modified_text[i:i+2] for i in range(0, len(modified_text), 2)]
    return digraphs

def create_cipher_grid(cipher_key):
    cipher_grid = [['' for _ in range(5)] for _ in range(5)]
    cipher_key = cipher_key.upper().replace('J', 'I')
    cipher_key_set = set()
    row, col = 0, 0
    for char in cipher_key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in cipher_key_set:
            cipher_grid[row][col] = char
            cipher_key_set.add(char)
            col += 1
            if col == 5:
                col = 0
                row += 1
    return cipher_grid

def find_char_position(grid, char):
    for row in range(5):
        for col in range(5):
            if grid[row][col] == char:
                return row, col

def encrypt_digraph_pair(grid, digraph):
    row1, col1 = find_char_position(grid, digraph[0])
    row2, col2 = find_char_position(grid, digraph[1])
    if row1 == row2:
        return grid[row1][(col1 + 1) % 5] + grid[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return grid[(row1 + 1) % 5][col1] + grid[(row2 + 1) % 5][col2]
    else:
        return grid[row1][col2] + grid[row2][col1]

def decrypt_digraph_pair(grid, digraph):
    row1, col1 = find_char_position(grid, digraph[0])
    row2, col2 = find_char_position(grid, digraph[1])
    if row1 == row2:
        return grid[row1][(col1 - 1) % 5] + grid[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return grid[(row1 - 1) % 5][col1] + grid[(row2 - 1) % 5][col2]
    else:
        return grid[row1][col2] + grid[row2][col1]

def playfair_cipher_algo(original_text, cipher_key, mode):
    cipher_grid = create_cipher_grid(cipher_key)
    processed_text = process_input_text(original_text)
    result = ''
    for digraph in processed_text:
        if mode == 'encrypt':
            result += encrypt_digraph_pair(cipher_grid, digraph)
        elif mode == 'decrypt':
            result += decrypt_digraph_pair(cipher_grid, digraph)
    return result

def get_user_input():
    cipher_key = input("Enter cipher keyword: ")
    original_text = input("Enter text to cipher: ")
    return original_text, cipher_key

user_text, user_key = get_user_input()
cipher_text = playfair_cipher_algo(user_text, user_key, 'encrypt')
print("Encrypted:", cipher_text)
decrypted_text = playfair_cipher_algo(cipher_text, user_key, 'decrypt')
print("Decrypted:", decrypted_text)