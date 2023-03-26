# Создайте функцию генератор чисел Фибоначчи.

def fibonacci(number: int):
    a, b = 0, 1
    for i in range(1, number + 1):
        if i > 2:
            c = a + b
            a, b = b, c
        elif i == 2:
            c = b
        else:
            c = a
        yield c


for i, num in enumerate(fibonacci(12), start=1):
    print(f'{i} число последовательности = {num}')
