import math


def affine(alphabet, text, key1, key2, type_e_d='e'):
    output = ""
    a1 = key1[0]
    b1 = key1[1]
    a2 = key2[0]
    b2 = key2[1]
    m = len(alphabet)
    if (math.gcd(a1, m) == 1) and (math.gcd(a2, m) == 1):
        a1_inv = pow(a1, -1, m)
        a2_inv = pow(a2, -1, m)
    else:
        return f"Пожалуйста, введите обратимые по модулю {m} параметры 'a1' и 'a2' в ключе, запустив программу заново."

    cnt = 0
    a_second = a_first = 0
    b_second = b_first = 0
    for elem in text:
        cnt += 1
        if cnt == 1:
            a = a_second = a1
            b = b_second = b1
            a_inv = a_inv_second = a1_inv
        elif cnt == 2:
            a = a_first = a2
            b = b_first = b2
            a_inv = a_inv_first = a2_inv
        else:
            a = (a_second * a_first) % m
            b = (b_second + b_first) % m
            a_inv = (a_inv_second * a_inv_first) % m

        ind = ord(elem) - ord(alphabet[0])
        if type_e_d == 'e':
            output += alphabet[(a * ind + b) % m]
        elif type_e_d == 'd':
            output += alphabet[((ind - b) * a_inv) % m]
        else:
            output = "Пожалуйста, в качестве обрабатываемого текста введите последовательность латинских символов заглавными буквами."
            break
        if cnt > 2:
            a_second = a_first
            b_second = b_first
            a_first = a
            b_first = b
            a_inv_second = a_inv_first
            a_inv_first = a_inv
    return output


alph_affine_r = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text_affine_r = input(
    "Введите в качестве обрабатываемого текста последовательность латинских символов в верхнем регистре: ")
key_1_affine_r = [int(param) for param in input(
    f"Введите через пробел в качестве 1-го ключа последовательно параметры 'a1' и 'b1'.\nОба параметра должны быть целыми числами, параметр 'a1' должен быть обратим по модулю {len(alph_affine_r)}: ").split()]
key_2_affine_r = [int(param) for param in input(
    f"Аналогично введите параметры 'a2' и 'b2' для 2-го ключа: ").split()]
type_e_d_affine_r = input(
    "Выберите режим: чтобы произвести зашифрование (encryption), введите «e» без кавычек; для расшифрования (decryption) – «d» аналогично: ")
print(affine(alph_affine_r, text_affine_r, key_1_affine_r, key_2_affine_r, type_e_d_affine_r))