plaintext = input("Enter plaintext: ")
width = int(input("Enter width: "))

# Padding
while len(plaintext) % width != 0:
    plaintext += "X"


# Encryption
cipher = ""

for i in range(width):
    cipher += plaintext[i::width]

print("Ciphertext:", cipher)


# Decryption
rows = len(cipher) // width
plain = ""

for i in range(rows):
    plain += cipher[i::rows]

print("Decrypted:", plain)