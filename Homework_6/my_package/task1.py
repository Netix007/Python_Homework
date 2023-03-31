""" Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""
from sys import argv


def _is_leap_year(year: int) -> bool:
    if str(year)[-2:] == '00':
        a = 400
    else:
        a = 4
    if year % a == 0:
        return True
    else:
        return False


def is_year_correct(text: str) -> bool:
    day, month, year = [int(x) for x in text.split('.')]
    if year < 1 or year > 9999:
        return False
    if month in (1, 3, 5, 7, 8, 10, 12) and 0 < day <= 31:
        return True
    if month in (4, 6, 9, 11) and 0 < day <= 30:
        return True
    if _is_leap_year(year):
        if month == 2 and 0 < day <= 29:
            return True
    else:
        if month == 2 and 0 < day <= 28:
            return True
    return False


if __name__ == '__main__':
    if len(argv) > 1:
        print(is_year_correct(argv[1]))
