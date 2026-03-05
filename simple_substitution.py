def simple_substitution(alphabet, text, key, type_e_d='e'):
    output = ""
    for elem in text:
        if (65 <= ord(elem) <= 90) or (elem == ' '):
            if elem == ' ':
                output += elem
            else:
                if type_e_d == 'e':
                    output += key[ord(elem) - ord(alphabet[0])]
                elif type_e_d == 'd':
                    output += alphabet[key.index(elem)]
                else:
                    output = "Пожалуйста, выберите режим зашифрования или расшифрования, перезапустив программу."
                    break
        else:
            output = "Пожалуйста, в качестве обрабатываемого текста введите последовательность латинских символов заглавными буквами.\nРазделителем слов может служить только пробел."
            break
    return output


alph_simple = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
flag_files = input("Работа с файлами (y) или ручной ввод (n)?")
if flag_files == 'y':
    inp_simple = input("Файл с исходным текстом: ")
    with open(f"{inp_simple}", 'r', encoding='utf-8') as inp_file:
        text_simple = inp_file.readline()
    key_simple = input(
        "Введите в качестве ключа последовательность, являющейся перестановкой символов латинского алфавита в верхнем регистре: ")
    type_e_d_simple = input(
        "Выберите режим: чтобы произвести зашифрование (encryption), введите «e» без кавычек; для расшифрования (decryption) – «d» аналогично: ")
    out_simple = input("Файл для полученного в ходе преобразований текста: ")
    out_text_simple = simple_substitution(alph_simple, text_simple, key_simple, type_e_d_simple)
    with open(f"{out_simple}", 'w') as out_file:
        out_file.write(out_text_simple)
else:
    text_simple = input(
        "Введите в качестве обрабатываемого текста последовательность латинских символов в верхнем регистре: ")
    key_simple = input(
        "Введите в качестве ключа последовательность, являющейся перестановкой символов латинского алфавита в верхнем регистре: ")
    type_e_d_simple = input(
        "Выберите режим: чтобы произвести зашифрование (encryption), введите «e» без кавычек; для расшифрования (decryption) – «d» аналогично: ")
print(simple_substitution(alph_simple, text_simple, key_simple, type_e_d_simple))