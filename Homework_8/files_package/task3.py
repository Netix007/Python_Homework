# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

import json
import csv


def json_to_csv(file_name: str) -> None:
    data_csv = []
    with open(file_name, 'r', encoding='UTF-8') as f:
        data = dict(json.load(f))
    for user_group, user_data in data.items():
        for user_id, user_name in user_data.items():
            my_row = [user_group, user_id, user_name]
            data_csv.append(my_row)
    with open('task3_csv.csv', 'w', newline='') as f_write:
        csv_write = csv.writer(f_write, dialect='excel', lineterminator="\r")
        csv_write.writerows(data_csv)


if __name__ == '__main__':
    json_to_csv('result_task2.json')
