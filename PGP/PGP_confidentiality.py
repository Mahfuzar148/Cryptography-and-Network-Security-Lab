from Crypto.PublicKey import RSA 
from Crypto.Cipher import AES, PKCS1_OAEP 
from Crypto.Random import get_random_bytes 
import base64 
import zlib 



# ------------ KEY GENERATION ------------

receiver_private = RSA.generate(1024) 
receiver_public = receiver_private.publickey()



# ------------ SENDER SIDE ------------

print("----------- Sender Side -----------")

M = "The name of my country is Bangladesh"



# Generate session key Ks

Ks = get_random_bytes(16)



# EC : Encrypt message using Ks

aes = AES.new(Ks, AES.MODE_EAX)

encrypted_M = aes.encrypt(
    M.encode()
)

nonce = aes.nonce



# EP : Encrypt Ks using receiver public key

rsa = PKCS1_OAEP.new(receiver_public)

encrypted_Ks = rsa.encrypt(Ks)



# Convert bytes to string

encrypted_Ks_text = base64.b64encode(encrypted_Ks).decode()

encrypted_M_text = base64.b64encode(encrypted_M).decode()

nonce_text = base64.b64encode(nonce).decode()



# Combine packet

packet = encrypted_Ks_text  + "|" + nonce_text + "|"+encrypted_M_text




# Compression

send_data = zlib.compress(packet.encode())


print("Message Sent")





# ------------ RECEIVER SIDE ------------

print("\n----------- Receiver Side -----------")



# Decompression

received_data = zlib.decompress(send_data).decode()



# Separate

encrypted_Ks_text, nonce_text, encrypted_M_text = received_data.split("|")



# Convert back to bytes

encrypted_Ks = base64.b64decode(encrypted_Ks_text)

nonce = base64.b64decode(nonce_text)

encrypted_M = base64.b64decode(encrypted_M_text)



# DP : Recover Ks

rsa = PKCS1_OAEP.new(receiver_private)

Ks = rsa.decrypt(encrypted_Ks)



# DC : Decrypt message

aes = AES.new(
    Ks,
    AES.MODE_EAX,
    nonce=nonce
)


original_M = aes.decrypt(encrypted_M)



print("Decrypted Message:")
print(original_M.decode())
