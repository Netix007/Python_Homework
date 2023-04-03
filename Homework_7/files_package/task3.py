# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# При достижении конца более короткого файла, возвращайтесь в его начало

FILE_RES_NAME = 'result.txt'


def my_func(file_num: str, file_name: str) -> None:
    with (open(file_num, 'r', encoding='UTF-8') as a,
            open(file_name, 'r', encoding='UTF-8') as b,
            open(FILE_RES_NAME, 'w', encoding='UTF-8') as c
          ):
        res_1 = [int(str(el).split('|')[0])*float(str(el).split('|')[1]) for el in list(a)]
        res_2 = [el[:-1] for el in list(b)]
        len_1, len_2 = len(res_1), len(res_2)
        max_len = max(len_1, len_2)
        i, j = 0, 0
        res_3 = []
        while True:
            if res_1[i] < 0:
                res_3.append(f'{str(res_2[j]).lower()} {abs(res_1[i])}')
            else:
                res_3.append(f'{str(res_2[j]).upper()} {round(res_1[i])}')
            c.write(res_3[-1] + '\n')
            i += 1
            j += 1
            if (len_1 == i == max_len) or (len_2 == j == max_len):
                break
            elif i == len_1:
                i = 0
                continue
            elif j == len_2:
                j = 0
                continue


if __name__ == '__main__':
    my_func('text.txt', 'names.txt')
