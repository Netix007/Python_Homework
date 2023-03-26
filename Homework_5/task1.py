# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def my_function(string: str) -> tuple:
    result = (string[:string.rfind('\\') + 1], *string[string.rfind('\\') + 1:].split('.'))
    return result


data = r'C:\Thecode\Media\test.txt'
print(*my_function(data))
