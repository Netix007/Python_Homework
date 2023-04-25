# Создайте класс окружность. Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.
import math


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
            raise TypeError('Радиус должен быть числом')
        if radius <= 0:
            raise ValueError('Значение радиуса должно быть положительное')
        self.radius = radius

    def circle_length(self) -> int | float:
        length = 2 * math.pi * self.radius
        return length

    def circle_square(self) -> int | float:
        square = math.pi * (self.radius ** 2)
        return square

    def __str__(self):
        return f'Окружность с радиусом {self.radius}'


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    # print(Circle(1))
