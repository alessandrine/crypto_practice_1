name_file_cipher = input("Файл с шифртекстом: ")

with open(f"{name_file_cipher}", 'r', encoding='utf-8') as file_cipher:
    ciphertext = file_cipher.readline()
'''============== СБОР СТАТИСТИКИ ПО ШИФРТЕКСТУ ==================='''
freq_dict = dict()
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    freq_dict.setdefault(letter, ciphertext.count(letter))
freq_dict_sorted = dict(sorted(freq_dict.items(), key=lambda item: item[-1], reverse=True))
print(freq_dict_sorted)

with open("output.txt", 'r', encoding='utf-8') as file_analysis:
    text_analysis = file_analysis.readline()
    freq_dict_lang = dict()
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        freq_dict_lang.setdefault(letter, text_analysis.count(letter))
    freq_dict_sorted_lang = dict(sorted(freq_dict_lang.items(), key=lambda item: item[-1], reverse=True))
freq_dict_sorted_lang_keys = list(freq_dict_sorted_lang.keys())

out_dict = dict()
cnt = 0
for element in list(freq_dict_sorted.keys()):
    out_dict.setdefault(freq_dict_sorted_lang_keys[cnt], element)
    cnt += 1

predict_key = ""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for symb in alphabet:
    predict_key += out_dict[symb]
print(predict_key)

output = ""
for elem in text_analysis:
    output += alphabet[predict_key.index(elem)]
print(output)