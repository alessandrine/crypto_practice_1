from itertools import permutations
from random import randint
from math import factorial


def simple_gen(num, alph):
    cnt = 0
    for x in permutations(alph):
        x = ''.join(x)
        if cnt < num:
            cnt += 1
        else:
            break
    return x


number = randint(1, factorial(11))
print(number)
print(simple_gen(number, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))