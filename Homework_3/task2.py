# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = list((1, 1, 1, 2, 3, 4, 4, 5, 6))
result1 = list()

for item in my_list:
    if my_list.count(item) != 1 and result1.count(item) == 0:
        result1.append(item)

if len(result1) != 0:
    print(f'Дублирующиеся элементы: {result1}')
else:
    print('Дублирующихся элементов нет')