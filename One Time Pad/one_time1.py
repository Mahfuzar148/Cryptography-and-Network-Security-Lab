

with open("One_time_pad/one_plain.txt","r") as file:
    text = file.read()

print(text)

with open("One_time_pad/one_key.txt","r") as file:
    key = file.read()

print(key)

plain = text.upper()
key = key.strip().upper()


alpha_count = 0

for ch in plain:
    if ch.isalpha():
        alpha_count +=1

if alpha_count>len(key):
    print("Key is too short")
    exit()
    
cipher = ""
key_ind = 0
for ch in plain:
   if ch.isalpha():
        p = ord(ch)-ord('A')
        k = ord(key[key_ind])-ord('A')
        value = (p+k)%26
        cipher += chr(value+ord('A'))
        key_ind +=1
   else:
       cipher +=ch
    
print("cipher text : ",cipher)

decrypted = ""
key_ind = 0
for ch in cipher:
   if ch.isalpha():
    c = ord(ch)-ord('A')
    k = ord(key[key_ind])-ord('A')
    value = (c-k)%26
    decrypted += chr(value+ord('A'))
    key_ind +=1
   else:
    decrypted +=ch
print("Decrypted text ",decrypted)

    
    