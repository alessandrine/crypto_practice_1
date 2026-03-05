# name_file_cipher = input("Файл с шифртекстом: ")
name_file_cipher = 'ciphertext-3.txt'
with open(f"{name_file_cipher}", 'r', encoding='utf-8') as file_cipher:
    ciphertext = file_cipher.readline()

name_file_plain = 'plaintext-3.txt'
with open(f"{name_file_plain}", 'r', encoding='utf-8') as file_plain:
    plaintext = file_plain.readline()

x = [ord(elem) - ord('A') for elem in plaintext]
y = [ord(elem) - ord('A') for elem in ciphertext]
print('x', x, '\n', 'y', y[:4], sep='\n')