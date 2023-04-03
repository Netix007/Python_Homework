# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры: расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.
import random
import os

VOWEL = 'aeiouyAEIOUY'
CONSONANT = 'bcdfghjklmnpqrstvwxBCDFGHJKLMNPQRSTVWX'
MIN_COUNT_V0WEL = 2
DIR_NAME = 'tmp'


def file_creator(expansion: str, min_name: int = 6, max_name: int = 30,
                 min_bytes: int = 256, max_bytes: int = 4096, count_files: int = 42) -> None:
    names = _gen_file_name(count_files, min_name, max_name)
    if DIR_NAME not in os.listdir():
        os.makedirs(f'{DIR_NAME}/')
    for el in names:
        with open(f'{DIR_NAME}/{el}.{expansion}', 'wb') as f:
            f.write(os.urandom(random.randint(min_bytes, max_bytes)))
    return


def _gen_file_name(count: int, min_name: int = 6, max_name: int = 30) -> list[str]:
    names = []
    for _ in range(count):
        name_length = random.randint(min_name, max_name)
        num_consonant = random.randint(0, name_length - MIN_COUNT_V0WEL)
        num_vowel = name_length - num_consonant
        simb = [random.choice(VOWEL) for _ in range(num_vowel)] + \
               [random.choice(CONSONANT) for _ in range(num_consonant)]
        random.shuffle(simb)
        names.append("".join(simb).capitalize())
    return names

if __name__ == '__main__':
    file_creator('hi', count_files=3)
