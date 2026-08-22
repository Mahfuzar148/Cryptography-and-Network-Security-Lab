from Crypto.PublicKey import RSA 
from Crypto.Cipher import AES, PKCS1_OAEP 
from Crypto.Hash import SHA256 
from Crypto.Signature import pkcs1_15 
from Crypto.Random import get_random_bytes 

import base64
import zlib



# ------------ KEY GENERATION ------------

# Sender key (Authentication)
sender_private = RSA.generate(1024)
sender_public = sender_private.publickey()


# Receiver key (Confidentiality)
receiver_private = RSA.generate(1024)
receiver_public = receiver_private.publickey()



# ------------ SENDER SIDE ------------

print("----------- Sender Side -----------")


M = "The name of my country is Bangladesh"



# -------- Authentication --------

# H(M)

hash_object = SHA256.new(M.encode())


# E(PRa,H(M))

signature = pkcs1_15.new(sender_private).sign(hash_object)



# Signature + Message

signed_message = (
    base64.b64encode(signature).decode()
    + "|"
    + M
)



# -------- Compression --------

compressed_data = zlib.compress(
    signed_message.encode()
)



# -------- Confidentiality --------


# Generate Ks

Ks = get_random_bytes(16)



# EC(compressed data, Ks)

aes = AES.new(
    Ks,
    AES.MODE_EAX
)


encrypted_data = aes.encrypt(
    compressed_data
)

nonce = aes.nonce



# E(KUb, Ks)

rsa = PKCS1_OAEP.new(receiver_public)

encrypted_Ks = rsa.encrypt(Ks)



# Send packet

packet = (
    base64.b64encode(encrypted_Ks).decode()
    + "|"
    + base64.b64encode(nonce).decode()
    + "|"
    + base64.b64encode(encrypted_data).decode()
)


print("Message Sent")





# ------------ RECEIVER SIDE ------------

print("\n----------- Receiver Side -----------")



# Separate packet

encrypted_Ks, nonce, encrypted_data = packet.split("|")



# Convert bytes

encrypted_Ks = base64.b64decode(encrypted_Ks)

nonce = base64.b64decode(nonce)

encrypted_data = base64.b64decode(encrypted_data)




# -------- Recover Ks --------


# DP(KRb, encrypted Ks)

rsa = PKCS1_OAEP.new(receiver_private)

Ks = rsa.decrypt(encrypted_Ks)



# -------- Decrypt --------


aes = AES.new(
    Ks,
    AES.MODE_EAX,
    nonce=nonce
)


compressed_data = aes.decrypt(
    encrypted_data
)



# -------- Decompression --------


signed_message = zlib.decompress(
    compressed_data
).decode()



# Separate signature and message

signature, received_message = signed_message.split("|")



signature = base64.b64decode(signature)



print("Received Message:")
print(received_message)




# -------- Authentication --------


new_hash = SHA256.new(
    received_message.encode()
)


try:

    pkcs1_15.new(sender_public).verify(
        new_hash,
        signature
    )

    print("\nPGP Authentication Successful")
    print("Confidentiality Successful")


except:

    print("\nAuthentication Failed")
