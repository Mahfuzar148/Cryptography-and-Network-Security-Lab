from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA 
from Crypto.Signature import pkcs1_15
import zlib 
import base64





private_key = RSA.generate(1024)
public_key = private_key.publickey()



message = "The name of my country is Bangladesh" 

hash_object = SHA256.new(message.encode())

signature = pkcs1_15.new(private_key).sign(hash_object)

signature_text = base64.b64encode(signature).decode()

packet = signature_text + "|"+message


send_data = zlib.compress(packet.encode())


#receiver 

received_data = zlib.decompress(send_data).decode()

received_signature,received_message = received_data.split("|")


try:
    pkcs1_15.new(public_key).verify(
        SHA256.new(received_message.encode()),
        base64.b64decode(received_signature)
    )
    print("Authentication Successful")
    print("Message:", received_message)
except:
    print("Authentication Failed")
    
    

