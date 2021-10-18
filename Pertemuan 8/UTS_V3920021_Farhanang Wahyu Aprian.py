import math 
plaintext = input("Masukan Plaintext : ")
key, keyA, keyB = input("Masukkan Key : "), int(input("Key A : ")), int(input("Key B : "))


#======================================= Vigenere Chiper Site ==========================================================

def keygenerator(Plaintext, key):
    key = list(key)
    if len(key) == len(Plaintext):
        return key
    else:
        for x in range(len(Plaintext)-len(key)):
            key.append(key[x % len(key)])
        key = ''.join(key)
        return key


def enkripsivignere(plaintext, key):
    key = keygenerator(plaintext, key)

    plaintext = list(plaintext)
    enkripsi = []
    for x in range(len(plaintext)):
        if plaintext[x].isalpha():
            if plaintext[x].isupper():
                hurufawal = ord("A")
                convert = (ord(plaintext[x])- hurufawal) + (ord(key[x].upper()) - hurufawal) 
                hasil = convert % 26
                hasil = chr(hasil + hurufawal)
                enkripsi.append(hasil)
            if plaintext[x].islower():
                hurufawal = ord("a")
                convert = (ord(plaintext[x])- hurufawal) + (ord(key[x].lower()) - hurufawal) 
                hasil = convert % 26
                hasil = chr(hasil + hurufawal)
                enkripsi.append(hasil)

        else:
            enkripsi.append(plaintext[x])
        
    return  "".join(enkripsi)


def deskripsivignere(chipertext, key):
    key = keygenerator(chipertext, key)
    plaintext = list(chipertext)
    deskripsi = []
    for x in range(len(plaintext)):
        if plaintext[x].isalpha():
            if plaintext[x].isupper():
                hurufawal = ord("A")
                convert = (ord(plaintext[x])- hurufawal) - (ord(key[x].upper()) - hurufawal) 
                hasil = convert % 26
                hasil = chr(hasil + hurufawal)
                deskripsi.append(hasil)
            if plaintext[x].islower():
                hurufawal = ord("a")
                convert = (ord(plaintext[x])- hurufawal) - (ord(key[x].lower()) - hurufawal) 
                hasil = convert % 26
                hasil = chr(hasil + hurufawal)
                deskripsi.append(hasil)
        else:
            deskripsi.append(plaintext[x])

    return "".join(deskripsi)





# ================================================== AFFINE CHIPER ========================================


def CheckMMI(keyA): 
    n = [1,3,5,7,9,11,15,17,19,21,23,25] 
    for i in n: 
        looping = (keyA * i) % 26 #Berfungsi untuk menampung nilai index i dan melakukan operasi modulus
        if looping == 1: # jika ketemu looping  yang memiliki nilai satu maka akan di return nilai i yang memenuhi kondisi
            return i
def EnkripsiAffine(plaintext, keyA,keyB): 
    hasil = [] 
    for x in plaintext: 
        if x.isalpha(): 
            if x.isupper(): 
                Type = ord("A") 
                perkata = ord(x) 
                operasi = perkata - Type 
                operasi1 = keyA*operasi+keyB 
                mod = operasi1 % 26 
                hasilakhir = chr(mod + Type) 
                hasil.append(hasilakhir) # melakukan penambahan data pada hasil
            else: # pengondisian jika alphabet merupakan alphabet kecil
                Type = ord("a") # sama seperti diatas yaitu sebagai patokan untuk menghitung
                perkata = ord(x)
                operasi = perkata - Type
                operasi1 = keyA*operasi+keyB
                mod = operasi1 % 26
                hasilakhir = chr(mod + Type)
                hasil.append(hasilakhir)
        else: 
            hasil.append(x) 
    return ''.join(hasil)

def DeskripsiAffine(plaintext, keyA,keyB): 
    hasil = [] 
    y = CheckMMI(keyA) 
    for x in plaintext: 
        if x.isalpha():
            if x.isupper():
                Type = ord("A")
                perkata = ord(x)
                operasi = perkata - Type
                operasi1 = y*(operasi-keyB)
                mod = operasi1 % 26
                hasilakhir = chr(mod + Type)
                hasil.append(hasilakhir)
            else:
                Type = ord("a")
                perkata = ord(x)
                operasi = perkata - Type
                operasi1 = y*(operasi-keyB)
                mod = operasi1 % 26 #melakukan operasi yaitu mengembalikan huruf ke semula
                hasilakhir = chr(mod + Type)
                hasil.append(hasilakhir)
        else:
            hasil.append(x)
    return ''.join(hasil) # merakit kembali tuple

if math.gcd(keyA, 26) == 1: 
    print("\n \n \n \n \n \n \n \n=============================================================")
    print("====================Vigenere Chiper==========================")
    print("Plaintext : " + plaintext)
    print("Key : " + key)
    enkripsivignere = enkripsivignere(plaintext, key)
    enkripsiaff = EnkripsiAffine(enkripsivignere, keyA, keyB)
    print("Enkripsi Vig+Aff : " + enkripsiaff)

    print("=================== Affine Chiper ===========================")
    print("Key A : " + str(keyA))
    print("Key B : " + str(keyB))
    deskripsiaff = DeskripsiAffine(enkripsiaff, keyA, keyB)
    deskripsivig = deskripsivignere(deskripsiaff, key)
    print("Deskripsi : " + deskripsivig)
    print("============================================================")
    print("Program Selesai :)")

    
    
    
else: #jika GCD key A bernilai bukan 1 maka
    print("Kunci A merupakan kunci jelek") # menunjukkan bahwa key A tidak dapat digunakan
    print("Program Selesai") # menunjukan program telah selesai

