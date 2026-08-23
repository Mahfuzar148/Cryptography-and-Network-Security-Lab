from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import zlib
import base64



# Original Message

message = "The name of my country is Bangladesh"


print("Original Message:")
print(message)



# Compression

compressed = zlib.compress(
    message.encode()
)



# Generate AES Key

key = get_random_bytes(16)



# Encryption

aes = AES.new(
    key,
    AES.MODE_ECB
)


cipher = aes.encrypt(
    pad(compressed, AES.block_size)
)


stored_data = base64.b64encode(cipher)


print("\nEncrypted Stored Data:")
print(stored_data)



# ---------------- Read From Storage ----------------


aes = AES.new(
    key,
    AES.MODE_ECB
)


decrypted = unpad(
    aes.decrypt(
        base64.b64decode(stored_data)
    ),
    AES.block_size
)



original = zlib.decompress(
    decrypted
)



print("\nDecrypted Message:")
print(original.decode())
