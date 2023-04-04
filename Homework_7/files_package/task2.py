# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# Полученные имена сохраните в файл.

import random

FILE_NAME = 'names.txt'
MIN_LEN = 4
MAX_LEN = 7
MIN_COUNT_V0WEL = 2
VOWEL = 'aeiouyAEIOUY'
CONSONANT = 'bcdfghjklmnpqrstvwxBCDFGHJKLMNPQRSTVWX'


def gen_file_name(count: int) -> None:
    with open(FILE_NAME, 'a', encoding='UTF-8') as f:
        for _ in range(count):
            name_length = random.randint(MIN_LEN, MAX_LEN)
            num_consonant = random.randint(0, name_length - MIN_COUNT_V0WEL)
            num_vowel = name_length - num_consonant
            simb = [random.choice(VOWEL) for _ in range(num_vowel)] + \
                   [random.choice(CONSONANT) for _ in range(num_consonant)]
            random.shuffle(simb)
            name = "".join(simb).capitalize()
            f.write(name + '\n')


gen_file_name(10)
