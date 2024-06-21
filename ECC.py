from tinyec import registry
from Crypto.Cipher import AES
import hashlib, secrets, binascii

def encrypt_AES_GCM(msg, secret_key):
    aes_cipher = AES.new(secret_key, AES.MODE_GCM)
    ciphertext, auth_tag = aes_cipher.encrypt_and_digest(msg)
    return (ciphertext, aes_cipher.nonce, auth_tag)

def decrypt_AES_GCM(ciphertext, nonce, auth_tag, secret_key):
    aes_cipher = AES.new(secret_key, AES.MODE_GCM, nonce)
    plaintext = aes_cipher.decrypt_and_verify(ciphertext, auth_tag)
    return plaintext

def ecc_point_to_256_bit_key(point):
    sha = hashlib.sha256(int.to_bytes(point.x, 32, 'big'))
    sha.update(int.to_bytes(point.y, 32, 'big'))
    return sha.digest()

curve = registry.get_curve('brainpoolP256r1')

def encrypt_ECC(msg, public_key):
    ciphertext_private_key = secrets.randbelow(curve.field.n)
    shared_ecc_key = ciphertext_private_key * public_key
    secret_key = ecc_point_to_256_bit_key(shared_ecc_key)
    ciphertext, nonce, auth_tag = encrypt_AES_GCM(msg, secret_key)
    ciphertext_public_key = ciphertext_private_key * curve.g
    return (ciphertext, nonce, auth_tag, ciphertext_public_key)

def decrypt_ECC(encrypted_msg, private_key):
    (ciphertext, nonce, auth_tag, ciphertext_public_key) = encrypted_msg
    shared_ecc_key = private_key * ciphertext_public_key
    secret_key = ecc_point_to_256_bit_key(shared_ecc_key)
    plaintext = decrypt_AES_GCM(ciphertext, nonce, auth_tag, secret_key)
    return plaintext

msg = b'Python' \
      b'program'
print("Original message:", msg)

private_key = secrets.randbelow(curve.field.n)
public_key = private_key * curve.g

encrypted_msg = encrypt_ECC(msg, public_key)
encrypted_msg_obj = {
    'ciphertext': binascii.hexlify(encrypted_msg[0]),
    'ciphertext_public_key': hex(encrypted_msg[3].x) + hex(encrypted_msg[3].y % 2)[2:]
}
print("Encrypted message:", encrypted_msg_obj)

decrypted_msg = decrypt_ECC(encrypted_msg, private_key)
print("Decrypted message:", decrypted_msg)