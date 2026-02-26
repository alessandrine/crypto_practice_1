import math


def affine(alphabet, text, key, type_e_d='e'):
    output = ""
    a = key[0]
    b = key[1]
    m = len(alphabet)
    if math.gcd(a, m) == 1:
        a_inv = pow(a, -1, m)
    else:
        return f"Пожалуйста, введите обратимый по модулю {m} параметр 'a' в ключе, запустив программу заново."
    for elem in text:
        ind = ord(elem) - ord(alphabet[0])
        if type_e_d == 'e':
            output += alphabet[(a * ind + b) % m]
        elif type_e_d == 'd':
            output += alphabet[((ind - b) * a_inv) % m]
        else:
            output = "Пожалуйста, в качестве обрабатываемого текста введите последовательность латинских символов заглавными буквами."
            break
    return output


alph_affine = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text_affine = input(
    "Введите в качестве обрабатываемого текста последовательность латинских символов в верхнем регистре: ")
key_affine = [int(param) for param in input(
    f"Введите через пробел в качестве ключа последовательно параметры 'a' и 'b'.\nОба параметра должны быть целыми числами, параметр 'a' должен быть обратим по модулю {len(alph_affine)}: ").split()]
type_e_d_affine = input(
    "Выберите режим: чтобы произвести зашифрование (encryption), введите «e» без кавычек; для расшифрования (decryption) – «d» аналогично: ")
print(affine(alph_affine, text_affine, key_affine, type_e_d_affine))