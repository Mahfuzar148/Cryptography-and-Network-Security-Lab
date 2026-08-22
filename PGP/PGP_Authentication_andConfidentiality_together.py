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


# E(PRa, H(M))

signature = pkcs1_15.new(sender_private).sign(hash_object)



# -------- Confidentiality --------


# Generate Ks

Ks = get_random_bytes(16)



# EC(M, Ks)

aes = AES.new(Ks, AES.MODE_EAX)

encrypted_message = aes.encrypt(
    M.encode()
)

nonce = aes.nonce



# E(KUb, Ks)

rsa = PKCS1_OAEP.new(receiver_public)

encrypted_Ks = rsa.encrypt(Ks)



# Convert bytes to string

packet = (
    base64.b64encode(encrypted_Ks).decode()
    + "|"
    + base64.b64encode(nonce).decode()
    + "|"
    + base64.b64encode(encrypted_message).decode()
    + "|"
    + base64.b64encode(signature).decode()
)



# Z compression

send_data = zlib.compress(packet.encode())


print("Message Sent")





# ------------ RECEIVER SIDE ------------

print("\n----------- Receiver Side -----------")



# Z^-1

received = zlib.decompress(send_data).decode()



encrypted_Ks, nonce, encrypted_message, signature = received.split("|")



# Back to bytes

encrypted_Ks = base64.b64decode(encrypted_Ks)

nonce = base64.b64decode(nonce)

encrypted_message = base64.b64decode(encrypted_message)

signature = base64.b64decode(signature)



# -------- Confidentiality --------


# DP(KRb, encrypted Ks)

rsa = PKCS1_OAEP.new(receiver_private)

Ks = rsa.decrypt(encrypted_Ks)



# DC(M)

aes = AES.new(
    Ks,
    AES.MODE_EAX,
    nonce=nonce
)


original_message = aes.decrypt(
    encrypted_message
).decode()



print("Received Message:")
print(original_message)




# -------- Authentication --------


# H(received message)

new_hash = SHA256.new(
    original_message.encode()
)



# Verify E(PUa, signature)

try:

    pkcs1_15.new(sender_public).verify(
        new_hash,
        signature
    )


    print("\nPGP Authentication Successful")
    print("Confidentiality Successful")


except:

    print("\nAuthentication Failed")
