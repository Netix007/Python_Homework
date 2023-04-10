# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл. Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени. Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа. При перезапуске функции уже записанные в файл данные должны сохраняться.

import json
import os


def my_function(file_name: str) -> None:
    all_id = set()
    data = {}
    if os.path.getsize(file_name) != 0:
        with open(file_name, 'r', encoding='UTF-8') as f:
            data = dict(json.load(f))
    while True:
        text = input('Введите имя, личный идентификатор и уровень доступа (от 1 до 7), '
                     'данные должны быть разделены пробелом: ')
        if text == '':
            break
        user_name, user_id, user_gr = text.split()
        if user_id in all_id:
            print(f'Пользователь с {id} уже существует, введите данные другого пользователя')
            continue
        if not 1 <= int(user_gr) <= 7:
            print('Уровень доступа должен быть в диапазоне от 1 до 7')
            continue
        all_id.add(user_id)
        (data.setdefault(user_gr, {}))[user_id] = user_name
        with open(file_name, 'w', encoding='UTF-8') as f:
            json.dump(data, f)


if __name__ == '__main__':
    my_function('result_task2.json')
