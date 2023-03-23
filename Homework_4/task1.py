# Напишите функцию для транспонирования матрицы.

def transponse_matrix(matrix: list[list[int | float]]):
    result = list()
    for i in range(len(matrix[0])):
        my_row = list(map(lambda x: x[i], matrix))
        result.append(my_row)
    return result


my_matrix = [[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8]]

transponse_matrix(my_matrix)
print(transponse_matrix(my_matrix))
