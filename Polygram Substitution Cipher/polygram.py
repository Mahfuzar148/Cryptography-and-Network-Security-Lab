RULE_FILE = "2_Encryption_Rules.txt"

encrypt = {}
dycrypt = {}

with open(RULE_FILE,"r") as file:
    for line in file:
        plain, cipher = line.split()
        encrypt[plain] = cipher
        dycrypt[cipher]= plain


text = input("Enter input: ")

text = text.upper()

text = text.replace(" ","")

while len(text)%3 !=0:
    text = text+"X"

cipher_text = ""
plain_text = ""

for i in range(0, len(text),3):
    block = text[i:i+3]
    cipher_text += encrypt[block] 
print("Chipher_Text: ",cipher_text)

for i in range(0, len(text),3):
    block = cipher_text[i:i+3]
    plain_text += dycrypt[block] 
print("Plain_Text: ",plain_text)
