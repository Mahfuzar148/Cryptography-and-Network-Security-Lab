from Crypto.PublicKey import RSA 
from Crypto.Cipher import AES, PKCS1_OAEP 
from Crypto.Random import get_random_bytes
import base64 
import zlib



# ---------------- KEY GENERATION ----------------

r_pr_key = RSA.generate(1024)
r_pub_key = r_pr_key.publickey()



# Original Message

M = "The name of my country is Bangladesh"



# ---------------- SENDER SIDE ----------------


# Generate Session Key Ks

Ks = get_random_bytes(16)



# Z : Compression

compressed_M = zlib.compress(
    M.encode()
)



# EC : Encrypt compressed message using Ks

aes = AES.new(
    Ks,
    AES.MODE_EAX
)


encrypted_m = aes.encrypt(
    compressed_M
)


nonce = aes.nonce



# EP : Encrypt Ks using Receiver Public Key

rsa = PKCS1_OAEP.new(
    r_pub_key
)


encrypted_Ks = rsa.encrypt(
    Ks
)



# Convert bytes to string

encrypted_m_text = base64.b64encode(
    encrypted_m
).decode()


nonce_text = base64.b64encode(
    nonce
).decode()


encrypted_Ks_text = base64.b64encode(
    encrypted_Ks
).decode()



# Packet = Encrypted Message + Nonce + Encrypted Session Key

packet = (
    encrypted_m_text 
    + "|"
    + nonce_text 
    + "|"
    + encrypted_Ks_text
)



print("Message Sent")




# ---------------- RECEIVER SIDE ----------------



# Separate packet

encrypted_m, nonce, encrypted_Ks = packet.split("|")



# Convert back to bytes

encrypted_m = base64.b64decode(
    encrypted_m
)


nonce = base64.b64decode(
    nonce
)


encrypted_Ks = base64.b64decode(
    encrypted_Ks
)



# DP : Recover Ks using private key

rsa = PKCS1_OAEP.new(
    r_pr_key
)


decrypted_Ks = rsa.decrypt(
    encrypted_Ks
)



# DC : Decrypt message

aes = AES.new(
    decrypted_Ks,
    AES.MODE_EAX,
    nonce=nonce
)


compressed_M = aes.decrypt(
    encrypted_m
)



# Z^-1 : Decompression

decrypted_M = zlib.decompress(
    compressed_M
)



print("Decrypted Message:")
print(decrypted_M.decode())
