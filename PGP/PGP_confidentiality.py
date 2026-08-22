from Crypto.PublicKey import RSA  
from Crypto.Cipher import AES, PKCS1_OAEP  
from Crypto.Random import get_random_bytes 
import base64  
import zlib 



# ---------------- KEY GENERATION ---------------- 

receiver_private_key = RSA.generate(1024) 
receiver_public_key = receiver_private_key.publickey()



# Original Message (M)

message = "The name of my country is Bangladesh"



# ---------------- SENDER SIDE ----------------


# Generate Session Key (Ks)

session_key = get_random_bytes(16)



# Z : Compression

compressed_message = zlib.compress(
    message.encode()
)



# EC : Encrypt Message using Session Key (Ks)

aes_cipher = AES.new(
    session_key,
    AES.MODE_EAX
)


encrypted_message = aes_cipher.encrypt(
    compressed_message
)


nonce = aes_cipher.nonce



# EP : Encrypt Session Key using Receiver Public Key

rsa_cipher = PKCS1_OAEP.new(
    receiver_public_key
)


encrypted_session_key = rsa_cipher.encrypt(
    session_key
)



# Convert bytes to string

encrypted_message_text = base64.b64encode(
    encrypted_message
).decode()


nonce_text = base64.b64encode(
    nonce
).decode()


encrypted_session_key_text = base64.b64encode(
    encrypted_session_key
).decode()



# Packet = E(KUb[Ks]) + Encrypted Message

packet = (
    encrypted_message_text
    + "|"
    + nonce_text
    + "|"
    + encrypted_session_key_text
)


print("Message Sent")




# ---------------- RECEIVER SIDE ----------------



# Separate packet

encrypted_message_text, nonce_text, encrypted_session_key_text = packet.split("|")



# Convert back to bytes

encrypted_message = base64.b64decode(
    encrypted_message_text
)


nonce = base64.b64decode(
    nonce_text
)


encrypted_session_key = base64.b64decode(
    encrypted_session_key_text
)



# DP : Recover Session Key using Private Key

rsa_cipher = PKCS1_OAEP.new(
    receiver_private_key
)


session_key = rsa_cipher.decrypt(
    encrypted_session_key
)



# DC : Decrypt Message using Session Key

aes_cipher = AES.new(
    session_key,
    AES.MODE_EAX,
    nonce=nonce
)


compressed_message = aes_cipher.decrypt(
    encrypted_message
)



# Z^-1 : Decompression

original_message = zlib.decompress(
    compressed_message
)



print("Decrypted Message:")
print(original_message.decode())
