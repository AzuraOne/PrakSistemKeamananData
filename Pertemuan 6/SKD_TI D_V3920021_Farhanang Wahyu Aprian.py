key = input("Masukkan Kunci: ") #input untuk kunci
key = key.replace(" ", "") #mengubah kunci agar tidak memiliki spasi
key = key.upper() # mengubah kunci menjadi huruf besar


def matriks(x, y, matrik):  #membuat fungsi matriks
    return [[matrik for i in range(x)] for j in range(y)] #membuat matriks yang akan direturnkan


result = list() # membuat list kosong
for c in key:  # menyimpan key
    if c not in result: 
        if c == 'J': #jika key c sama dengan J akan diubah menjadi I
            result.append('I')
        else:
            result.append(c) # key c akan tetap dengan key yang sama
acuan = 0
for i in range(65, 91):  # menyimpan karakter besar
    if chr(i) not in result:
        if i == 73 and chr(74) not in result:
            result.append("I")
            acuan = 1
        elif acuan == 0 and i == 73 or i == 74:
            pass
        else:
            result.append(chr(i))
k = 0
my_matrix = matriks(5, 5, 0)  # mengatur matriks
for i in range(0, 5):  # Membuat Matriks
    for j in range(0, 5):
        my_matrix[i][j] = result[k]
        k += 1


def locindex(c):  # Mendapatkan lokasi tiap huruf
    loc = list()
    if c == 'J':
        c = 'I'
    for i, j in enumerate(my_matrix):
        for k, l in enumerate(j):
            if c == l:
                loc.append(i)
                loc.append(k)
                return loc


def enkripsi():  # Encryption
    msg = str(input("Masukkan Pesan : "))
    msg = msg.upper()
    msg = msg.replace(" ", "")
    i = 0
    for s in range(0, len(msg)+1, 2):
        if s < len(msg)-1:
            if msg[s] == msg[s+1]:
                msg = msg[:s+1]+'X'+msg[s+1:]
    if len(msg) % 2 != 0:
        msg = msg[:]+'X'
    print("Chipper Text : ", end=' ')
    while i < len(msg):
        loc = list()
        loc = locindex(msg[i])
        loc1 = list()
        loc1 = locindex(msg[i+1])
        if loc[1] == loc1[1]:
            print("{}{}".format(
                my_matrix[(loc[0]+1) % 5][loc[1]], my_matrix[(loc1[0]+1) % 5][loc1[1]]), end=' ')
        elif loc[0] == loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(
                loc[1]+1) % 5], my_matrix[loc1[0]][(loc1[1]+1) % 5]), end=' ')
        else:
            print("{}{}".format(
                my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]]), end=' ')
        i = i+2


def deskripsi():  # Deskripsi
    msg = str(input("Masukkan Chiper Text: "))
    msg = msg.upper()
    msg = msg.replace(" ", "")
    print("Plain Text : ", end=' ')
    i = 0
    while i < len(msg):
        loc = list()
        loc = locindex(msg[i])
        loc1 = list()
        loc1 = locindex(msg[i+1])
        if loc[1] == loc1[1]:
            print("{}{}".format(
                my_matrix[(loc[0]-1) % 5][loc[1]], my_matrix[(loc1[0]-1) % 5][loc1[1]]), end=' ')
        elif loc[0] == loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(
                loc[1]-1) % 5], my_matrix[loc1[0]][(loc1[1]-1) % 5]), end=' ')
        else:
            print("{}{}".format(
                my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]]), end=' ')
        i = i+2


while(1):
    pilih = int(input("\n 1.Enkripsi: \n 2.Deskripsi: \n 3.Keluar \n"))
    if pilih == 1:
        enkripsi()
    elif pilih == 2:
        deskripsi()
    elif pilih == 3:
        exit()
    else:
        print("Pilihlah yang tersedia")
