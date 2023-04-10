# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
import json
import random
from typing import Callable


def coef_from_csv(file_name: str):
    def deco(func: Callable):
        res_dict = []

        def wrapper(**kwargs):
            with open(file_name, 'r', newline='') as f:
                csv_file = csv.reader(f, dialect='excel-tab')
                for line in csv_file:
                    args = (int(i) for i in line)
                    res_dict.append(func(*args, **kwargs))
            return res_dict
        return wrapper
    return deco


def save_to_json(func: Callable):
    file = 'result.json'

    def wrapper(*args, **kwargs):
        with open(file, 'w', encoding='UTF-8') as json_f:
            json.dump(func(*args, **kwargs), json_f, indent=2)

    return wrapper


@save_to_json
@coef_from_csv('coef.csv')
def quadratic_equation(a: int, b: int, c: int):
    coef_str = f'{a} {b} {c}'
    if a == 0 and b != 0:
        res_str = f'Уравнение не квадратное! Корень: {-c / b}'
    elif a == 0 and b == 0:
        res_str = f'Это не уравнение!'
    else:
        discr = b**2 - 4 * a * c
        if discr > 0:
            x1 = (-b + discr**0.5) / (2 * a)
            x2 = (-b - discr**0.5) / (2 * a)
            res_str = f'Корни уравнения: {x1}, {x2}'
        elif discr == 0:
            x = -b / (2 * a)
            res_str = f'Корень уравнения: {x}'
        else:
            res_str = 'Действительных корней нет'
    res_dict = {coef_str: res_str}
    return res_dict


def csv_creator(file_name: str, string_count: int) -> None:
    all_coef = []
    for i in range(string_count):
        coef = [random.randint(-100, 100) for _ in range(3)]
        all_coef.append(coef)
    with open(file_name, 'w', newline='') as f:
        csv_writer = csv.writer(f, dialect='excel-tab', lineterminator="\r")
        csv_writer.writerows(all_coef)


if __name__ == '__main__':
    csv_creator('coef.csv', 10)
    quadratic_equation()
