# Создайте функцию-замыкание, которая запрашивает два целых числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
import random
from typing import Callable

MIN_NUM = 1
MAX_NUM = 100
MIN_COUNT = 1
MAX_COUNT = 10


def deco(func: Callable):

    def wrapper(num, count):
        if not MIN_NUM <= num <= MAX_NUM:
            num = random.randint(1, 100)
        if not MIN_COUNT <= count <= MAX_COUNT:
            count = random.randint(1, 10)
        result = func(num, count)
        return result

    return wrapper


@deco
def guess_number(num: int, count: int) -> None:
    print(f'Угадайте число, у вас {count} попыток')
    for i in range(1, count + 1):
        input_num = int(input(f'Попытка № {i}: '))
        if input_num == num:
            print('Поздравляем, вы угадали число')
            break
        elif input_num < num:
            print(f'Загаданное число больше {input_num}')
        else:
            print(f'Загаданное число меньше {input_num}')
    else:
        print(f'К сожалению угадать число не удалось. Было загадано число {num}')
    return


if __name__ == '__main__':
    guess_number(1000, 9)
