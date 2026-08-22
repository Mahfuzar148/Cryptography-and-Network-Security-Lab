import hashlib

message = input("Enter message: ")

digest = hashlib.sha256(
    message.encode('utf-8')
).hexdigest()

print("The hexadecimal equivalent of hash is:", digest)
