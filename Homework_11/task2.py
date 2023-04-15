# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее созданных экземпляров
# сохраняются в пару списков-архивов list-архивы также являются свойствами экземпляра
# Добавьте строки документации для класса.
# Добавьте методы представления экземпляра для программиста и для пользователя.
class Archive:
    """
    Класс архив, хранит пару - число и строку. При создании нового экземпляра класса, старые данные
    из ранее созданных экземпляров сохраняются в пару списков-архивов list-архивы.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.list_num = []
            cls._instance.list_string = []
        else:
            cls._instance.list_num.append(cls._instance.num)
            cls._instance.list_string.append(cls._instance.string)
        return cls._instance

    def __init__(self, num, string):
        self.num = num
        self.string = string

    def __str__(self):
        return f'Экземпляр класса Archive с данными. Число: {a.num}\tСтрока: {a.string} ' \
               f'Лист-архив чисел: {a.list_num}\tЛист-архив строк: {a.list_string}'

    def __repr__(self):
        return f'Archive({a.num = }, {a.string = }, {a.list_num = }, {a.list_string = }'


if __name__ == '__main__':
    a = Archive(3, 'test')
    print(a)
    print(f'{a = }')
