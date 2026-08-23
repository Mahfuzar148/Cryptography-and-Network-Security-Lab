from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import zlib
import base64



# -------- Keys --------

sender_private = RSA.generate(1024)
sender_public = sender_private.publickey()

receiver_private = RSA.generate(1024)
receiver_public = receiver_private.publickey()



# -------- Sender --------

message = "The name of my country is Bangladesh"


# Hash

hash_obj = SHA256.new(
    message.encode()
)


# Signature

signature = pkcs1_15.new(
    sender_private
).sign(hash_obj)



# Signature + Message

data = (
    base64.b64encode(signature).decode()
    + "|"
    + message
)



# Compression

compressed = zlib.compress(
    data.encode()
)



# Generate AES Session Key

Ks = get_random_bytes(16)



# AES Encryption

aes = AES.new(
    Ks,
    AES.MODE_ECB
)


cipher = aes.encrypt(
    pad(compressed,AES.block_size)
)



# Encrypt AES Key using Receiver Public Key

rsa = PKCS1_OAEP.new(
    receiver_public
)


encrypted_key = rsa.encrypt(Ks)



# Packet

packet = (
    base64.b64encode(cipher).decode()
    +
    "|"
    +
    base64.b64encode(encrypted_key).decode()
)



print("Message Sent")




# -------- Receiver --------


cipher, encrypted_key = packet.split("|")


cipher = base64.b64decode(cipher)

encrypted_key = base64.b64decode(encrypted_key)



# Recover AES Key

rsa = PKCS1_OAEP.new(
    receiver_private
)


Ks = rsa.decrypt(
    encrypted_key
)



# AES Decrypt

aes = AES.new(
    Ks,
    AES.MODE_ECB
)


compressed = unpad(
    aes.decrypt(cipher),
    AES.block_size
)



data = zlib.decompress(
    compressed
).decode()



signature,message = data.split("|")



print("\nReceived Message:")
print(message)



# Verify Signature

signature = base64.b64decode(signature)


new_hash = SHA256.new(
    message.encode()
)



try:

    pkcs1_15.new(sender_public).verify(
        new_hash,
        signature
    )

    print("\nAuthentication and Confidentiality Successful")


except:

    print("Failed")
