# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен расширяться, а не перезаписываться. Каждый ключевой параметр
# сохраните как отдельный ключ json словаря. Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы. Имя файла должно совпадать с именем декорируемой
# функции.
import json
from typing import Callable


def deco(func: Callable) -> Callable:
    json_file = f'{func.__name__}.json'
    data = []
    with open(json_file, 'r', encoding='UTF-8') as f_r:
        data = json.load(f_r)

    def wrapper(*args, **kwargs):
        result = func(args, kwargs)
        # json_file = f'{func.__name__}.json'
        json_dict = {'args': args, **kwargs, 'res': result}
        data.append(json_dict)
        with open(json_file, 'w', encoding='UTF-8') as f:
            json.dump(data, f)
        return result

    return wrapper


@deco
def dec_func(*args, **kwargs):
    print(f'Запуск функции с параметрами {args}, {kwargs}')
    return


if __name__ == '__main__':
    dec_func([1, 2, 3], human='Alex', fish=["Larry", "Curly", "Moe"])
