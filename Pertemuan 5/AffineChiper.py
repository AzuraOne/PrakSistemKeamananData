import math # Mengimport modul math
plaintext = input("Insert your text to encrypt : ") #berfungsi untuk tempat input text yang dienkript
keyA = int(input("Insert A Key : ")) #berfungsi untuk memasukkan Key A
keyB = int(input("Insert B Key : ")) #berfungsi untuk memasukkan Key B




def MMI(keyA): #Function yang berfungsi untuk mengatur MMI berdasarkan Key A yang diinputkan
    n = [1,3,5,7,9,11,15,17,19,21,23,25] #berfungsi untuk menampung nilai N 
    for i in n: #Melakukan looping array  n
        looping = (keyA * i) % 26 #Berfungsi untuk menampung nilai index i dan melakukan operasi modulus
        if looping == 1: # jika ketemu looping  yang memiliki nilai satu maka akan di return nilai i yang memenuhi kondisi
            return i


def Enkripsi(plaintext, keyA,keyB): #melakukan enkripsi yang memiliki paramter plaintext, key A , key B
    hasil = [] # berfungsi untuk menjadi wadah pada hasil
    for x in plaintext: # Melakukan looping kata plaintext sebagai x
        if x.isalpha(): # Mengecheck apakah yang diloopiing merupakan alphabet jika alphabet maka akan diteruskan
            if x.isupper(): # mengecheck apakah yang dilooping merupakan huruf kapital jika iya maka akan dijalankan
                Type = ord("A") # berfungsi untuk patokan angka
                perkata = ord(x) #nilai x akan diubah menjadi nilai ascii
                operasi = perkata - Type #melakukan pengurangan kata nilai ascii ke nilai murni
                operasi1 = keyA*operasi+keyB #melakukan operasi affinechiper yaitu mengkalikan key A dengan operasi lalu dijumlah dengan key B
                mod = operasi1 % 26 # Melakukan perhitungan modulus pada nilai x
                hasilakhir = chr(mod + Type) # mengubah kembali menjadi character dan diubah ke nilai ascii semula
                hasil.append(hasilakhir) # melakukan penambahan data pada hasil
            else: # pengondisian jika alphabet merupakan alphabet kecil
                Type = ord("a") # sama seperti diatas yaitu sebagai patokan untuk menghitung
                perkata = ord(x)
                operasi = perkata - Type
                operasi1 = keyA*operasi+keyB
                mod = operasi1 % 26
                hasilakhir = chr(mod + Type)
                hasil.append(hasilakhir)
        else: #berfungsi untuk pengondisian jika x merupakan bukan alphabet
            hasil.append(x) # menambahkan x ke tuple hasil
    return ''.join(hasil) # mengubah tuple hasil menjadi string

def Deskripsi(plaintext, keyA,keyB): #function yang berfungsi untuk menampilkan hasil
    hasil = [] # sebagai penampungan
    y = MMI(keyA) # menentukan nilai y berdasarkan function MMI
    for x in plaintext: # melakukan looping seperti enkripsi
        if x.isalpha():
            if x.isupper():
                Type = ord("A")
                perkata = ord(x)
                operasi = perkata - Type
                operasi1 = y*(operasi-keyB) # melakukan operasi yaitu mengembalikan huruf ke semula 
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

if math.gcd(keyA, 26) == 1: #mengecheck apakah GCD key a sama dengan nilai 1
    print("========================================================================")
    print("Plaintext :" + plaintext) # Menampilkan Plaintext yang diinputkan
    enkripsi = Enkripsi(plaintext,keyA,keyB) # melakukan enkripsi
    print("Key A :" + str(keyA) ) #menampilkan key A yang dibuat

    print("key B :" + str(keyB)) # menampilkan key B yang dibuat 

    print("Enkripsi : " + enkripsi) # menampilkan huruf yang di enkripsi

    deskripsi = Deskripsi(enkripsi, keyA, keyB) # melakukan deskripsi
    print("Deskripsi : " + deskripsi) # menampilkan text yang dideskripsi
    print("========================================================================")
    print("Program finished") # tanda untuk mengetahui program telah selesai
    
else: #jika GCD key A bernilai bukan 1 maka
    print("A key is bad") # menunjukkan bahwa key A tidak dapat digunakan
    print("Program finished") # menunjukan program telah selesai



