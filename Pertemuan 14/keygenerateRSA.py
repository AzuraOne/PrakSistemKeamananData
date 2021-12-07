from Crypto.PublicKey import RSA
import random

# Mengatur nama kunci
namegenerator = input("Masukkan Nama Kunci Private : ")
unique = random.randint(0, 999) # Mengatur random
finalname = namegenerator + str(unique)  # mengabungkan uniq dan nama

key = RSA.generate(2048) # melakukan generate RSA key
private_key = key.exportKey() # melakukan export kunci
file_out = open("private"+ finalname+".txt", "wb") # melakukn operasi pada file
file_out.write(private_key) # melakukan write pda file
file_out.close() # file dimatikan

public_key = key.publickey().exportKey() # melakukan export public key
file_out = open("receiver"+ finalname+".txt", "wb") # melakukan export receiver/ public key
file_out.write(public_key) # menambahkan isi key pada file
file_out.close() # file ditutup