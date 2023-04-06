# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.

import json


def create_json(file_name: str) -> None:
    with (
        open(file_name, 'r', encoding='UTF-8') as a,
        open('result_json.json', 'w', encoding='UTF-8') as b
    ):
        res = [tuple(line[0:-1].split()) for line in a]
        my_dict = dict([(x.capitalize(), y) for x, y in res])
        json.dump(my_dict, b, indent=1, ensure_ascii=False)


if __name__ == '__main__':
    create_json('result_task3.txt')
