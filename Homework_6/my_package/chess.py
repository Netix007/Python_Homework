"""Шахматный модуль. Предназначен для решения задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга возвращает истину, а если бьют - ложь. Содержит функцию для случайной расстановки ферзей.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""
import random


def _is_beat_two(first: tuple, second: tuple) -> bool:
    if first[0] == second[0] or first[1] == second[1]:
        return False
    if abs(first[0] - second[0]) == abs(first[1] - second[1]):
        return False
    return True


def is_beat(chess_pieces: list[tuple]) -> bool:
    pieces = len(chess_pieces)
    for i in range(pieces - 1):
        for j in range(i + 1, pieces):
            if not _is_beat_two(chess_pieces[i], chess_pieces[j]):
                return False
    return True


def random_chess_pieces(start=0, result=None):
    desk = [(i, j) for i in range(8) for j in range(8)]
    if result is None:
        result = [random.choice(desk)]
        desk.remove(result[0])

    for i in range(start, len(desk)):
        result.append(desk[i])
        if is_beat(result):
            if len(result) == 8:
                break
            else:
                random_chess_pieces(i + 1, result)
        else:
            result.pop(-1)
    if len(result) != 8:
        result.pop(-1)
    return result


if __name__ == '__main__':
    output = []
    while len(output) != 4:
        elem = set(random_chess_pieces())
        if elem not in output:
            output.append(elem)
    print(*output, sep="\n")
