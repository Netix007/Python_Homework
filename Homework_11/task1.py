# Создайте класс Моя Строка, где: будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)
# Добавьте строки документации для класса.
import datetime


class MyString(str):
    """
    Класс расширение класса str. Позволяет хранить имя автора и дату создания строки.
    """
    def __new__(cls, string, author_name):
        instance = super().__new__(cls, string)
        instance.author_name = author_name
        instance.create_time = datetime.datetime.now().strftime('%H:%M:%S')
        return instance

    def __str__(self):
        return f'{self.create_time} {self.author_name}: {super().__str__()}'


if __name__ == '__main__':
    text = MyString('Hello world!!!', 'Alex')
    print(text)
