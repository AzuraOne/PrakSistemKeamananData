import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
import ast
random_generator = Random.new().read
# menggenerate kunci publik dan kunci private
key = RSA.generate(1024, random_generator)

publickey = key.publickey()  # ekspor kunci publik untuk ditukarkan
privatekey = open("public.pem", "wb")
privatekey.write(publickey.exportKey())
privatekey.close()
# ENKRIPSI
encryptor = PKCS1_OAEP.new(publickey)  # menggunakan instansi dari PKCS1_OAEP

name = input("masukkan nama file : ")
plaintext = open(name, "rb")

encrypted = encryptor.encrypt(bytes(plaintext.read()))  # pesan untuk dienkripsi
plaintext.close()# menampilkan hasil enkripsi

# Update file .txt

enkripsi = open(name, 'wb')
enkripsi.write(encrypted)
enkripsi.close()


# Dekripsi
decryptor = PKCS1_OAEP.new(key)
privatekey = open("private.pem", "wb")
privatekey.write(key.exportKey())
privatekey.close()
# melakukan dekripsi dari pesan yang dienkripsi
decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))

encrypt = open('dekripsi.txt', 'wb')  # buka file txt, 'w' adalah write
encrypt.write(decrypted)  # menambahkan hasil dekripsi
encrypt.close()
