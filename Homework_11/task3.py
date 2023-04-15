# Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника. Складываем и вычитаем периметры,
# а не длинну и ширину. При вычитании не допускайте отрицательных значений.
# Добавьте сравнение прямоугольников по площади. Должны работать все шесть операций сравнения

class Rectangle:
    """Клас Прямоугольник. Позволяет осуществлять операции с прямоугольниками."""
    def __init__(self, length: int | float, width: int | float | None = None):
        self.width = width or length
        self.length = length

    def get_perimeter(self) -> int | float:
        perimeter = 2 * (self.length + self.width)
        return perimeter

    def get_square(self) -> int | float:
        square = self.length * self.width
        return square

    def __str__(self):
        return f'Прямоугольник со сторонами {self.length} и {self.width}'

    def __add__(self, other):
        a = self.length
        b = (self.get_perimeter() + other.get_perimeter() - 2 * a) / 2
        return Rectangle(a, b)

    def __sub__(self, other):
        per1 = self.get_perimeter()
        per2 = other.get_perimeter()
        if per1 < per2:
            a = (per2 - per1) / 10
            b = (per2 - per1 - 2 * a) / 2
        else:
            a = (per1 - per2) / 10
            b = (per1 - per2 - 2 * a) / 2
        return Rectangle(a, b)

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __gt__(self, other):
        return self.get_square() > other.get_square()

    def __ge__(self, other):
        return self.get_square() >= other.get_square()


if __name__ == "__main__":
    rectangle1 = Rectangle(2, 4)
    print(rectangle1.get_square())
    rectangle2 = Rectangle(5, 2)
    print(rectangle2.get_square())
    print(rectangle1 <= rectangle2)
