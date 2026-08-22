# -----------------------------------------
# One Time Pad Cipher
# Keep Space and Special Characters
# -----------------------------------------


# Read plaintext file

with open("One_time_pad/one_plain.txt", "r") as file:
    text = file.read()



# Read key file

with open("One_time_pad/one_key.txt", "r") as file:
    key = file.read().strip().upper()



# Convert plaintext to uppercase
plain = text.upper()



# Check key length
# Only alphabet characters need key

alpha_count = 0

for ch in plain:
    if ch.isalpha():
        alpha_count += 1


if len(key) < alpha_count:

    print("Key is too short!")
    exit()



# -----------------------------------------
# Encryption
# -----------------------------------------

cipher = ""

key_index = 0


for ch in plain:


    # Encrypt only alphabet

    if ch.isalpha():


        # Plain character value
        p = ord(ch) - ord('A')


        # Key character value
        k = ord(key[key_index]) - ord('A')


        # Encryption formula
        value = (p + k) % 26


        # Number to character
        cipher += chr(value + ord('A'))


        # Move to next key character
        key_index += 1


    else:

        # Keep space and symbols unchanged
        cipher += ch



print("Ciphertext:", cipher)



# -----------------------------------------
# Decryption
# -----------------------------------------

decrypted = ""

key_index = 0



for ch in cipher:


    if ch.isalpha():


        # Cipher character value
        c = ord(ch) - ord('A')


        # Key character value
        k = ord(key[key_index]) - ord('A')


        # Decryption formula
        value = (c - k) % 26


        # Number to character
        decrypted += chr(value + ord('A'))


        key_index += 1


    else:

        # Keep space and symbols unchanged
        decrypted += ch



print("Decrypted:", decrypted)
