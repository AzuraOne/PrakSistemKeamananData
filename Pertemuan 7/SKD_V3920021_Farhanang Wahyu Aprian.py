import numpy as np  # Melakukan import modul numpy
from egcd import egcd  # Melakukan import modul egcd

# Membuat variabel alfabet yang menampung 26 karakter alfabet
alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Membuat fungsi yang mengubah index menjadi karakter dan sebaliknya
letter_to_index = dict(zip(alfabet, range(len(alfabet))))
index_to_letter = dict(zip(range(len(alfabet)), alfabet))

# Membuat fungsi fungsi untuk melakukan operasi hitung terhdap matrix
def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = egcd(det, modulus)[1] % modulus
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )

    return matrix_modulus_inv


# Membuat fungsi enkripsi untuk plaintext
def enkripsi(message, K):
    encrypted = ""
    message_in_numbers = []

    for letter in message:
        message_in_numbers.append(letter_to_index[letter])

    split_P = [
        message_in_numbers[i: i + int(K.shape[0])]
        for i in range(0, len(message_in_numbers), int(K.shape[0]))
    ]

    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]

        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter_to_index[" "])[:, np.newaxis]

        numbers = np.dot(K, P) % len(alfabet)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            encrypted += index_to_letter[number]

    return encrypted

# Membuat fungsi enkripsi pada plaintext
def dekripsi(cipher, Kinv):
    decrypted = ""
    cipher_in_numbers = []

    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])

    split_C = [
        cipher_in_numbers[i: i + int(Kinv.shape[0])]
        for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))
    ]

    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numbers = np.dot(Kinv, C) % len(alfabet)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += index_to_letter[number]

    return decrypted

# Fungsi main yang mana memberikan pemulaian enkripsi dan deskripsi
def main():
    message = "FARHANANGWAHYUAPRIAN"

    K = np.matrix([[2, 3], [1, 6]])
    Kinv = matrix_mod_inv(K, len(alfabet))

    encrypted_message = enkripsi(message, K)
    decrypted_message = dekripsi(encrypted_message, Kinv)

    print("Plaintext: " + message)
    print("Enkripsi: " + encrypted_message)
    print("Deckripsi: " + decrypted_message)

main()