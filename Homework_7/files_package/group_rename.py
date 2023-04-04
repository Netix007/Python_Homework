# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
import os

DIR_NAME = 'tmp/'


def group_rename_files(expansion: str, res_expansion: str, start_val: int, stop_val: int,
                       count_num: int = 4, res_file_name: str = '') -> None:
    file_list = [el for el in os.listdir(DIR_NAME) if os.path.isfile(os.path.join(DIR_NAME, el))]
    count = 1
    for obj in file_list:
        file_name = obj.split('.')[0]
        file_exp = obj.split('.')[1]
        if file_exp == expansion:
            new_file = f'{file_name[start_val-1:stop_val]}{res_file_name}' \
                       f'{_generate_num(count_num, count)}.{res_expansion}'
            os.rename(f'{DIR_NAME}{obj}', f'{DIR_NAME}{new_file}')
            count += 1
            print(obj)
    print(file_list)
    return


def _generate_num(count_num: int, num: int) -> str:
    len_num = len(str(num))
    result = '0'*(count_num-len_num) + str(num)
    return result


if __name__ == '__main__':
    group_rename_files('nu', 'bu', 3, 7, res_file_name="result")
