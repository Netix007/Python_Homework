# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.
import random

NUM_FROM = -1000
NUM_TO = 1000


def add_random_num(num_string: int, file_name: str) -> None:
    with open(f'{file_name}.txt', 'a', encoding='utf-8') as f:
        for _ in range(num_string):
            f.write(f'{random.randint(NUM_FROM, NUM_TO)}|{random.uniform(NUM_FROM,NUM_TO)}\n')


add_random_num(10, "text")
