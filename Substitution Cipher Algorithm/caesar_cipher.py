# Encryption Function
def encrypt(text, shift):
    result = ""

    # Normalize shift
    shift = shift % 26

    for ch in text:
        # Uppercase letters
        if ch.isupper():
            new_char = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            result += new_char

        # Lowercase letters
        elif ch.islower():
            new_char = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            result += new_char

        # Other characters (space, number, symbol)
        else:
            result += ch

    return result


# Decryption Function
def decrypt(text, shift):
    result = ""

    shift = shift % 26

    for ch in text:
        # Uppercase letters
        if ch.isupper():
            new_char = chr((ord(ch) - ord('A') - shift + 26) % 26 + ord('A'))
            result += new_char

        # Lowercase letters
        elif ch.islower():
            new_char = chr((ord(ch) - ord('a') - shift + 26) % 26 + ord('a'))
            result += new_char

        # Other characters
        else:
            result += ch

    return result


# Main Program
text = input("Enter text: ")
shift = int(input("Enter shift value: "))

# Encryption
encrypted = encrypt(text, shift)
print("Encrypted Text:", encrypted)

# Decryption
decrypted = decrypt(encrypted, shift)
print("Decrypted Text:", decrypted)