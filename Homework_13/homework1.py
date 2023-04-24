# Создайте класс окружность. Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.
import math


class CircleRadiusError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Радиус окружности должен быть положительным числом. Вы ввели: {self.value}'


class Circle:

    def __init__(self, radius: int | float):
        if (type(radius) == float or type(radius) == int) and radius > 0:
            self.radius = radius
        else:
            raise CircleRadiusError(radius)

    def circle_length(self) -> int | float:
        length = 2 * math.pi * self.radius
        return length

    def circle_square(self) -> int | float:
        square = math.pi * (self.radius ** 2)
        return square

    def __str__(self):
        return f'Окружность с радиусом {self.radius}'


if __name__ == '__main__':
    my_circle = Circle(3)
    print(my_circle)
