# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
import csv


class MyDec:

    MY_DICT = {'_first_name': 'Имя', '_last_name': 'Отчество', '_patronymic': 'Фамилия'}

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять.')

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Поле \'{self.MY_DICT[self.param_name]}\' должно быть строкой')
        if not value.isalpha():
            raise ValueError(f'Поле \'{self.MY_DICT[self.param_name]}\' должно содержать только буквы')
        if not value[0].isupper():
            raise ValueError(f'Поле \'{self.MY_DICT[self.param_name]}\' должно начинаться с заглавной буквы')


class CsvReader:
    def __init__(self, file_name: str):
        self._data = {}
        with open(file_name, 'r', newline='') as f:
            csv_file = csv.reader(f)
            for row in csv_file:
                self._data[row[0]] = {'оценки': [], 'тесты': []}

    @property
    def get_data(self):
        return self._data


class Student:

    first_name = MyDec()
    last_name = MyDec()
    patronymic = MyDec()

    def __init__(self, first_name: str, last_name: str, patronymic: str, file_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self._assessment = CsvReader(file_name).get_data

    def __str__(self):
        return f'Студент: {self.patronymic} {self.first_name} {self.last_name} {self._assessment}'

    def add_assessment(self, subject: str, type_assessment: str, result: int):
        if subject not in self._assessment:
            ValueError(f'Студент {self.patronymic} не изучает {subject}')
        if type_assessment not in self._assessment[subject]:
            raise ValueError('Можно добавить только "оценки" или "тесты"')
        if not isinstance(result, int):
            raise TypeError('Результаты студента должны быть целым числом')
        if type_assessment == 'оценки':
            if 2 <= result <= 5:
                self._assessment[subject][type_assessment].append(result)
            else:
                raise ValueError('Оценки должны быть от 2 до 5')
        else:
            if 0 <= result <= 100:
                self._assessment[subject][type_assessment].append(result)
            else:
                raise ValueError('Результаты теста должны быть от 0 до 100')

    def average_tests(self):
        result_dict = {}
        for subject in self._assessment:
            res_score = 0
            for score in self._assessment[subject]['тесты']:
                res_score += score
            if len(self._assessment[subject]['тесты']) != 0:
                result_dict[subject] = res_score/len(self._assessment[subject]['тесты'])
            else:
                result_dict[subject] = 0
        return f'Средний балл по тестам: {result_dict}'

    def average_scores(self):
        result = 0
        count = 0
        for subject in self._assessment:
            if sum(self._assessment[subject]['оценки']) != 0:
                result += sum(self._assessment[subject]['оценки'])
                count += 1
        if count == 0:
            result = 0
        else:
            result = result / count
        return f'Средний балл по оценкам всех предметов вместе взятых: {result}'


if __name__ == '__main__':
    student1 = Student('Ivan', 'Ivanovich', 'Ivanov', 'Ivanov.csv')
    student1.add_assessment('математика', 'тесты', 60)
    student1.add_assessment('математика', 'тесты', 20)
    student1.add_assessment('математика', 'оценки', 5)
    student1.add_assessment('физика', 'оценки', 4)
    print(student1.average_tests())
    print(student1.average_scores())
    print(student1)
