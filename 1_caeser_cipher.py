



def encript(text):
    cipher = ""
    for ch in text:
        if ch.isalpha():
           if ch.isupper():
               cipher += chr((ord(ch)-ord('A')+3)%26+ord('A'))
           else:
               cipher += chr((ord(ch)-ord('a')+3)%26+ord('a'))
        else :
            cipher += ch
    
    return cipher


def decrypt(text):
    plain = ""
    for ch in text:
        if ch.isalpha():
           if ch.isupper():
               plain += chr((ord(ch)-ord('A')-3)%26+ord('A'))
           else:
               plain += chr((ord(ch)-ord('a')-3)%26+ord('a'))
        else :
            plain += ch
    
    return plain




plain_text = input("Enter plain text : ")

cipher_text =encript(plain_text)

plain = decrypt(cipher_text)

print("Cipher text : ",cipher_text)
print("Decrypted text : ",plain)
        
    


