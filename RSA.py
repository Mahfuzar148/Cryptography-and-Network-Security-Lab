m = str(6882326879666683)
e = 79
d = 1019
n = 3337



b_size = len(str(n))-1

cipher = []
cipher_text =""
for i in range(0,len(m),b_size):
  block = int(m[i:i+b_size])
  encrypt =pow(block,e,n)
  cipher.append(encrypt)
  cipher_text +=str(encrypt)


print("cipher text : ",cipher_text)

decrypted = ""

for i in cipher:
    block = pow(i,d,n)
    decrypted += str(block)

print("decrypted text : ",decrypted)
