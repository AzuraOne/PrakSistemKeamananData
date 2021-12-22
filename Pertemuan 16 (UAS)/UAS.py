#Mengimport Library
import os
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES #import kriptografi AES


nama = input("Masukkan nama file") # Ketik download.jpg
#Mengambil nilai kunci atau Key
def getKey(keysize):
    key = os.urandom(keysize) # Melakukan byte random dengan size dari keysize

    return key


def getIV(blocksize):
    iv = os.urandom(blocksize) # Melakukan byte Random dengan byte random dari blocksize
    return iv

#fungsi enkripsi gambar
def encrypt_image(filename, key, iv): # fungsi untuk
    BLOCKSIZE = 16 # panjang blok 16
    encrypted_filename = "encrypted_" + filename #enkripsi nama file gambar ditambah dengan encypted_ di depannya

    with open(filename, "rb") as file1: #open gambar
        data = file1.read() # Membaca file1

# program untuk enkripsi gambar dengan AES
        cipher = AES.new(key, AES.MODE_CBC, iv) # melakukan enkripsi dengan aes mode CBC dan menginputkan iV
        ciphertext = cipher.encrypt(pad(data, BLOCKSIZE))

        with open(encrypted_filename, "wb") as file2: # membuka file encrypted_filename tadi sebagai file 2
            file2.write(ciphertext) # menulis lagi yang terenkripsi ke file 2
    return encrypted_filename # Mengembalikan filename terenkripsi

# tahap dekripsi sama seperti enkripsi naum berbeda di proses dekripsi dari file gambar tersebut
def decrypt_image(filename, key, iv):
    BLOCKSIZE = 16 # Melakukan mengatur block pada blocksize
    decrypted_filename = "decrypted_" + filename # melakukan dekripsi

    with open(filename, "rb") as file1:
        data = file1.read() # Membaca file  terdeskripsi

        cipher2 = AES.new(key, AES.MODE_CBC, iv) # Melakukan new
        decrypted_data = unpad(cipher2.decrypt(data), BLOCKSIZE) #proses Deskripsi

        with open(decrypted_filename, "wb") as file2:
            file2.write(decrypted_data) # Melakukan dekripsi data dan meuliskan file2

    return decrypted_filename # mengembalikan dekripsi file nama


KEYSIZE = 16 # key yang digunakan
BLOCKSIZE = 16 # panjang blok 
filename = nama #file foto yang ingin di enkripsi atau deskripsi

key = getKey(KEYSIZE) #variable untuk pengambilan dari nilai KEYSZISE
iv = getIV(BLOCKSIZE) #variable untuk pengambilan dari nilai BLOCKSIZE

encrypted_filename = encrypt_image(filename, key, iv) # Function untuk memamggil function enkripsi untuk dibaca
decrypted_filename = decrypt_image(encrypted_filename, key, iv) # melakukan deskripsi 
