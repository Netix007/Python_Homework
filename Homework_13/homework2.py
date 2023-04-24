# Создайте класс Матрица. Добавьте методы для:
# вывода на печать, сравнения, сложения, умножения матриц

class MatrixError(Exception):
    pass


class MatrixMultError(MatrixError):
    def __init__(self, matrix_a: int, matrix_b: int):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b

    def __str__(self):
        return f'Матрицы нельзя умножить, число столбцов матрицы A - {self.matrix_a} ' \
               f'не совпадает с числом строк матрицы B - {self.matrix_b}!'


class MatrixSumError(MatrixError):
    def __init__(self, matrix_a: tuple, matrix_b: tuple):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b

    def __str__(self):
        return f'Матрицы разного размера. Матрица A - [{self.matrix_a[0]} x {self.matrix_a[1]}], ' \
               f'Матрица В - [{self.matrix_b[0]} x {self.matrix_b[1]}]. Сложение невозможно!'


class Matrix:
    """
    Класс матрица, позволяет выполтять математические действия с матрицами.
    """

    def __init__(self, my_matrix: list[list[int]]):
        """Добавляет свойство my_matrix классу"""
        self.my_matrix = my_matrix

    def __str__(self):
        """Строчное представление матрицы."""
        return '\n'.join(['\t'.join([str(it) for it in el]) for el in self.my_matrix])

    def __eq__(self, other):
        """Сравнение матриц (операция равенства)."""
        return self.__str__() == other.__str__()

    def __gt__(self, other):
        """Сравнение матриц (операция больше)."""
        return len(self.my_matrix) * len(self.my_matrix[0]) > len(other.my_matrix) * len(other.my_matrix[0])

    def __ge__(self, other):
        """Сравнение матриц (операция не больше)."""
        return len(self.my_matrix) * len(self.my_matrix[0]) <= len(other.my_matrix) * len(other.my_matrix[0])

    def __add__(self, other):
        """Вычисление суммы матриц. Выкидывает исключение при невозможности осуществить операцию суммирования."""
        result = []
        if len(self.my_matrix) != len(other.my_matrix) or len(self.my_matrix[0]) != len(other.my_matrix[0]):
            raise MatrixSumError((len(self.my_matrix[0]), len(self.my_matrix)),
                                 (len(other.my_matrix[0]), len(other.my_matrix)))
        for i in range(len(self.my_matrix)):
            row = []
            for j in range(len(self.my_matrix[0])):
                row.append(self.my_matrix[i][j] + other.my_matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        """Вычисление произведения матриц. Выкидывает исключение при невозможности осуществить операцию умножения."""
        result = []
        if len(self.my_matrix[0]) != len(other.my_matrix):
            raise MatrixMultError(len(self.my_matrix[0]), len(other.my_matrix))
        for i in range(len(self.my_matrix)):
            row = []
            for j in range(len(other.my_matrix[0])):
                elem = 0
                for k in range(len(other.my_matrix)):
                    elem += self.my_matrix[i][k] * other.my_matrix[k][j]
                row.append(elem)
            result.append(row)
        return Matrix(result)

    def sum_elem(self):
        """Суммирует все элементы матрицы."""
        return sum([sum(elem) for elem in self.my_matrix])


if __name__ == '__main__':
    matrixA = [[1, -2, 3], [4, 1, 7]]
    matrixB = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    matrixC = [[-9, 1, 0], [4, 1, 1], [-2, 2, -1]]
    matrixD = [[4, 5, 6], [7, 8, 9], [10, 11, 12]]

    print(Matrix(matrixA))
    print(Matrix(matrixB) + Matrix(matrixC))
