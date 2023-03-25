# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def dict_gen(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, set | list | dict):
            my_dict[str(value)] = key
        else:
            my_dict[value] = key
    return my_dict


my_set = [1, 2, 3]
print(dict_gen(химия=1, физика=4, математика=3, физра=my_set))
