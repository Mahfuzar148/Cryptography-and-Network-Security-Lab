import hashlib
message = input("Enter name : ")


digest = hashlib.md5(
    message.encode('utf-8')
).hexdigest()

print("The hexadecimal equivalent of hash is : ", digest)
