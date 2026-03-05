# name_file_cipher = input("Файл с шифртекстом: ")
name_file_cipher = 'ciphertext-2.txt'

def word_pattern(word):
    pattern = []
    pat_dict = dict()
    k = 0
    for let in word:
        if let not in list(pat_dict.keys()):
            pat_dict.setdefault(let, k)
            k += 1
    for let in word:
        pattern.append(str(pat_dict[let]))
    return '.'.join(pattern)

def pattern_word_sample(num, d):
    out_d = dict()
    for pair in d.items():
        if len(pair[-1]) == num:
            out_d.setdefault(pair[0], pair[-1])
    return out_d


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

# Словарь из книги CrackingCodes
with open("dictionary_al_swiergat.txt", 'r') as words_lang_file:
    words_lang = []
    for word in words_lang_file:
        words_lang.append(word.strip())

print("THI* (dict): ", [word for word in words_lang if (word[0:3] == 'THI') and (len(word) == 4)]) # THIN THIS
pred_dict['L'] = ['N', 'S']

'''=================== РАБОТА С ПАТТЕРНАМИ СЛОВ В СЛОВАРЕ ЯЗЫКА ===================='''
w_with_pat_lang = []
for word in words_lang:
    w_with_pat_lang.append([word_pattern(word), word])
grouped_pat_lang = dict()
set_keys_pat_lang = set([x[0] for x in w_with_pat_lang])
for pat in set_keys_pat_lang:
    grouped_pat_lang.setdefault(pat, [])
for pair in w_with_pat_lang:
    grouped_pat_lang[pair[0]].append(pair[-1])
'''=================== РАБОТА С ПАТТЕРНАМИ СЛОВ В ШИФРТЕКСТЕ ===================='''
w_with_pat_ciph = []
for word in cipher_list:
    w_with_pat_ciph.append([word_pattern(word), word])
grouped_pat_ciph = dict()
set_keys_pat_ciph = set([x[0] for x in w_with_pat_ciph])
for pat in set_keys_pat_ciph:
    grouped_pat_ciph.setdefault(pat, [])
for pair in w_with_pat_ciph:
    grouped_pat_ciph[pair[0]].append(pair[-1])

# Сделаем выборку из паттернов с 1 подходящим словом
one_word_grouped_pat_lang = pattern_word_sample(1, grouped_pat_lang)
one_word_grouped_pat_ciph = pattern_word_sample(1, grouped_pat_ciph)
# Словарь предположений, но уже по сопоставлению слов
word_pred = dict()
for pat_1 in one_word_grouped_pat_ciph.keys():
    if pat_1 in one_word_grouped_pat_lang.keys():
        word_pred.setdefault(one_word_grouped_pat_ciph[pat_1][0], one_word_grouped_pat_lang[pat_1][0])

# Перенос в словарь предположений по буквам
for pair in word_pred.items():
    key = pair[0]
    value = pair[1]
    for ind in range(len(key)):
        if (key[ind] not in 'OQITZ') and (value[ind] not in 'ETAIH'):
            if value[ind] not in pred_dict[key[ind]]:
                pred_dict[key[ind]].append(value[ind])

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