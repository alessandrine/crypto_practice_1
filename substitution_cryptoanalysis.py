# name_file_cipher = input("Файл с шифртекстом: ")
name_file_cipher = 'ciphertext-2.txt'

with open(f"{name_file_cipher}", 'r', encoding='utf-8') as file_cipher:
    ciphertext = file_cipher.readline()
'''============== СЛОВА В ШИФРТЕКСТЕ ===================='''
cipher_list = [word for word in ciphertext.split()]
'''============== СБОР СТАТИСТИКИ ПО ШИФРТЕКСТУ ==================='''
freq_dict = dict()
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    freq_dict.setdefault(letter, ciphertext.count(letter))
freq_dict_sorted = dict(sorted(freq_dict.items(), key=lambda item: item[-1], reverse=True))
print("Статистика по шифртексту:\n", freq_dict_sorted)

'''============== СБОР СТАТИСТИКИ ПО ЯЗЫКУ ==================='''
with open("output.txt", 'r', encoding='utf-8') as file_analysis:
    text_analysis = file_analysis.readline()
    freq_dict_lang = dict()
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        freq_dict_lang.setdefault(letter, text_analysis.count(letter))
    freq_dict_sorted_lang = dict(sorted(freq_dict_lang.items(), key=lambda item: item[-1], reverse=True))
freq_dict_sorted_lang_keys = list(freq_dict_sorted_lang.keys())
print("Статистика по языку:\n", freq_dict_sorted_lang)

'''================ СЛОВАРЬ ПРЕДПОЛОЖЕНИЙ ======================'''
# Ключами являются буквы шифртекста, значениями – кандидаты для их расшифровки
pred_dict = dict()
for symb in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    pred_dict.setdefault(symb, [])
# На основании частотного анализа предположим:
pred_dict['T'].append('E')
pred_dict['Z'].append('T')
# Анализ слов в тексте
# 1 буква - I или A
print("1 буква: ", _:=set([word for word in cipher_list if len(word) == 1]))
for let in _:
    pred_dict[let].append('I')
    pred_dict[let].append('A')
# Проба для THIS, THAT
print("T**T: ", t__t:=set([word for word in cipher_list if (len(word) == 4) and (word[0] == word[-1] == 'Z')]))
print("TH**: ", th__:=set([word for word in cipher_list if (len(word) == 4) and (word[0] == 'Z') and (word[1] == 'I')]))
print("TH*: ", th_:=set([word for word in cipher_list if (len(word) == 3) and (word[0] == 'Z') and (word[1] == 'I')]))
pred_dict['I'].append('H')
pred_dict['Q'] = ['A']
pred_dict['O'] = ['I']



print("Словарь предположений: ", pred_dict)

# '''================= ПОПЫТКА СОПОСТАВЛЕНИЯ ==================='''
# out_dict = dict()
# cnt = 0
# for element in list(freq_dict_sorted.keys()):
#     out_dict.setdefault(freq_dict_sorted_lang_keys[cnt], element)
#     cnt += 1
# print(out_dict)

# predict_key = ""
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for symb in alphabet:
#     predict_key += out_dict[symb]
# print(predict_key)
#
# output = ""
# for elem in text_analysis:
#     output += alphabet[predict_key.index(elem)]
# print(output)