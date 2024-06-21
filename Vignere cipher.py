def custom_encrypt(text, secret):
    encrypted_result = ""
    secret_repeated = (secret * (len(text) // len(secret))) + secret[:len(text) % len(secret)]
    for i in range(len(text)):
        if text[i].isalpha():
            text_num = ord(text[i]) - ord('A')
            secret_num = ord(secret_repeated[i]) - ord('A')
            encrypted_num = (text_num + secret_num) % 26
            encrypted_result += chr(encrypted_num + ord('A'))
        else:
            encrypted_result += text[i]
    return encrypted_result


def custom_decrypt(encrypted_text, secret):
    decrypted_result = ""
    secret_repeated = (secret * (len(encrypted_text) // len(secret))) + secret[:len(encrypted_text) % len(secret)]
    for i in range(len(encrypted_text)):
        if encrypted_text[i].isalpha():
            encrypted_num = ord(encrypted_text[i]) - ord('A')
            secret_num = ord(secret_repeated[i]) - ord('A')
            decrypted_num = (encrypted_num - secret_num) % 26
            decrypted_result += chr(decrypted_num + ord('A'))
        else:
            decrypted_result += encrypted_text[i]
    return decrypted_result


if __name__ == "__main__":
    secret_key = input("Enter the secret key: ").upper()
    input_data = input("Enter the data for encryption: ").upper()
    encrypted_data = custom_encrypt(input_data, secret_key)
    print(f"Original Data: {input_data}")
    print(f"Encrypted Data: Ciphered Text={encrypted_data}")
    decrypted_data = custom_decrypt(encrypted_data, secret_key)
    print(f"Decrypted Data: Original Text={decrypted_data}")