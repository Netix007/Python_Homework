# Создайте класс окружность. Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.
import math
import logging
import argparse

logging.basicConfig(filename='homework1.log', encoding='utf-8', filemode='w', level=logging.INFO)
logger = logging.getLogger('main')


class Circle:
    """
        Класс окружность. Создание окружности с заданным радиусом.
        >>> Circle(1).circle_length()
        6.283185307179586
        >>> Circle(1).circle_square()
        3.141592653589793
        >>> Circle('1')
        Traceback (most recent call last):
            ...
        TypeError: Радиус должен быть числом
        >>> Circle(-100)
        Traceback (most recent call last):
            ...
        ValueError: Значение радиуса должно быть положительное
        >>> print(Circle(1))
        Окружность с радиусом 1
    """

    def __init__(self, radius: int | float):
        if not isinstance(radius, float | int):
            logger.error('Попытка создания окружности с недопустимыми параметрами (радиус не число)')
            raise TypeError('Радиус должен быть числом')
        if radius <= 0:
            logger.error('Попытка создания окружности с недопустимыми параметрами (задан отрицательный радиус)')
            raise ValueError('Значение радиуса должно быть положительное')
        self.radius = radius
        logger.info(f'Создана окружность с радиусом {radius}')

    def circle_length(self) -> int | float:
        length = 2 * math.pi * self.radius
        logger.info(f'Вычислена длинна окружности (результат вычисления - {length})')
        return length

    def circle_square(self) -> int | float:
        square = math.pi * (self.radius ** 2)
        logger.info(f'Вычислена площадь окружности (результат вычисления - {square})')
        return square

    def __str__(self):
        return f'Окружность с радиусом {self.radius}'


def get_arg():
    arg = argparse.ArgumentParser(description='Получаем аргументы')
    arg.add_argument("-r", "--radius", type=int, help='введите радиус окружности', default=1)
    arg_res = arg.parse_args()
    return Circle(arg_res.radius)


if __name__ == '__main__':
    print(Circle(1))
    print(get_arg())
