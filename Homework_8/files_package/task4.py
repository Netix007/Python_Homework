# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями. В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора. Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь. Имя исходного и конечного файлов передавайте как аргументы
# функции.

import csv
import json


def csv_json(file_name_csv: str, file_name_json: str) -> None:

    with (
        open(file_name_csv, 'r', newline='') as f,
        open(file_name_json, 'w', encoding='UTF-8') as a
    ):
        csv_file = csv.reader(f, dialect='excel')
        all_data = []
        for line in csv_file:
            user_gr, user_id, user_name = line
            if len(user_id) < 10:
                user_id = '0'*(10-len(user_id)) + user_id
            user_hash = hash((user_name, user_id))
            data = {'id': user_id, 'level': user_gr, 'name': user_name, 'hash': user_hash}
            all_data.append(data)
        json.dump(all_data, a, ensure_ascii=False,  indent=2)


if __name__ == '__main__':
    csv_json('task3_csv.csv', 'task4_json.json')
