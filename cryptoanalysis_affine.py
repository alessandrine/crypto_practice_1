name_file_cipher = input("Файл с шифртекстом: ")

with open(f"{name_file_cipher}", 'r', encoding='utf-8') as file_cipher:
    ciphertext = file_cipher.readline()
'''============== СБОР СТАТИСТИКИ ПО ШИФРТЕКСТУ ==================='''
freq_dict = dict()
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    freq_dict.setdefault(letter, ciphertext.count(letter))
freq_dict_sorted = dict(sorted(freq_dict.items(), key=lambda item: item[-1], reverse=True))
print(freq_dict_sorted)
'''============== ПРЕДПОЛОЖЕНИЕ ПО ПЕРВЫМ 2 БУКВАМ ==================='''
freq_keys = list(freq_dict_sorted.keys())
enc_1 = ord(freq_keys[0]) - ord('A')
enc_2 = ord(freq_keys[1]) - ord('A')
dec_1 = ord('E') - ord('A') # for getting indexes in the alphabet
dec_2 = ord('T') - ord('A')
a = ((enc_1 - enc_2) * pow((dec_1 - dec_2), -1, 26)) % 26
b = (enc_1 - (a * dec_1)) % 26
print(f"Полученные a, b равны {a, b} соотвественно")
'''============== ПОПЫТКА РАСШИФРОВАНИЯ (КЛЮЧ УЗНАЛИ) ==================='''
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a_inv = pow(a, -1, 26)
decr_message = ''
for elem in ciphertext:
    ind = ord(elem) - ord('A')
    decr_message += alphabet[((ind - b) * a_inv) % 26]
print(decr_message)
name_decr_file = input("Файл для записи дешифрованного варианта текста: ")
with open(f"{name_decr_file}", 'w') as decr_file:
    decr_file.write(decr_message)