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
text_simple = input(
    "Введите в качестве обрабатываемого текста последовательность латинских символов в верхнем регистре: ")
key_simple = input(
    "Введите в качестве ключа последовательность, являющейся перестановкой символов латинского алфавита в верхнем регистре: ")
type_e_d_simple = input(
    "Выберите режим: чтобы произвести зашифрование (encryption), введите «e» без кавычек; для расшифрования (decryption) – «d» аналогично: ")
print(simple_substitution(alph_simple, text_simple, key_simple, type_e_d_simple))
