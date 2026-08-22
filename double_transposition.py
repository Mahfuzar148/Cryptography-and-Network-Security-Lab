def encrypt(text, width):
    # Padding
    while len(text) % width != 0:
        text += 'X'

    # Write row-wise, read column-wise
    cipher = ""

    for i in range(width):
        cipher += text[i::width]

    return cipher


def decrypt(cipher, width):
    rows = len(cipher) // width
    text = ""

    # Reverse column-wise transposition
    for i in range(rows):
        text += cipher[i::rows]

    return text


# ---------------- MAIN ----------------

plaintext = input("Enter plaintext: ")

width1 = int(input("Enter first width: "))
width2 = int(input("Enter second width: "))

# First transposition
cipher1 = encrypt(plaintext, width1)

# Second transposition
cipher2 = encrypt(cipher1, width2)

print("\nAfter First Transposition:", cipher1)
print("Final Ciphertext:", cipher2)


# ---------------- DECRYPTION ----------------

# Reverse second transposition
text1 = decrypt(cipher2, width2)

# Reverse first transposition
text2 = decrypt(text1, width1)

print("After Reverse Transposition:", text1)
print("Original Plaintext:", text2)