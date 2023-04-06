# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
import json
import csv
import pickle
import os
from pathlib import Path


def file_explorer(dir_path: str, dir_list=None) -> (list, int):
    if dir_list is None:
        dir_list = []
    parent_dir = Path(dir_path).parent.name
    full_size = 0
    for obj in os.listdir(dir_path):
        path_el = dir_path + '\\' + obj
        if os.path.isdir(path_el):
            obj_type = 'Директория'
            dir_dict = {'Объект': obj, 'Родительская директория': parent_dir, 'Тип объекта': obj_type,
                        'Размер в байтах': None}
            dir_list.append(dir_dict)
            dir_dict['Размер в байтах'] = file_explorer(path_el, dir_list)[1]
        elif os.path.isfile(path_el):
            obj_type = 'Файл'
            size = os.path.getsize(path_el)
            full_size += size
            dir_dict = {'Объект': obj, 'Родительская директория': Path(path_el).parent.name, 'Тип объекта': obj_type,
                        'Размер в байтах': size}
            dir_list.append(dir_dict)
    else:
        return dir_list, full_size


def data_to_json_v1(data: list) -> None:
    with open('homework_json', 'w', encoding='UTF-8') as f:
        my_dict = {}
        for elem in data:
            my_dict.setdefault(elem['Родительская директория'], {}).setdefault(elem['Тип объекта'], {})[
                elem['Объект']] = elem['Размер в байтах']
        json.dump(my_dict, f, indent=2, ensure_ascii=False)


def data_to_json_v2(data: list) -> None:
    with open('homework_json', 'w', encoding='UTF-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def data_to_csv(data: list) -> None:
    with open('homework_csv', 'w', newline='', encoding='utf-8') as f:
        data_csv_all = []
        for elem in data:
            data_csv = [elem['Родительская директория'], elem['Объект'], elem['Тип объекта'], elem['Размер в байтах']]
            data_csv_all.append(data_csv)
        csv_write = csv.writer(f, dialect='excel', lineterminator="\r")
        csv_write.writerows(data_csv_all)


def data_to_pickle(data: list) -> None:
    with open('homework_pickle.pickle', 'wb') as f:
        pickle.dump(data, f)


if __name__ == '__main__':
    my_link = r'C:\Users\kino_\OneDrive\Документы\учеба\Network'
    res_data = file_explorer(my_link)[0]
    data_to_json_v2(res_data)
    data_to_csv(res_data)
    data_to_pickle(res_data)
