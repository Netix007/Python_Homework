# Создайте класс-фабрику. Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа. Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.


class Animal:
    def __init__(self, class_name, age, weight):
        self.name = class_name
        self.age = age
        self.weight = weight


class Fish(Animal):
    def __init__(self, class_name, age, weight, swim_speed):
        super().__init__(class_name, age, weight)
        self.swim_speed = swim_speed

    def class_differences(self):
        print(f'Рыба может плавать со скоростью: {self.swim_speed}')


class Bird(Animal):
    def __init__(self, class_name, age, weight, fly_speed):
        super().__init__(class_name, age, weight)
        self.fly_speed = fly_speed

    def class_differences(self):
        print(f'Птица может летать со скоростью: {self.fly_speed}')


class Reptile(Animal):
    def __init__(self, class_name, age, weight, number_paws):
        super().__init__(class_name, age, weight)
        self.number_paws = number_paws

    def class_differences(self):
        print(f'У рептилии {self.number_paws} лап')


class AnimalFactory:
    def __init__(self, class_name, age, weight, *args):
        if class_name == 'fish':
            self.create_animal = Fish(class_name, age, weight, *args)
        elif class_name == 'bird':
            self.create_animal = Bird(class_name, age, weight, *args)
        else:
            self.create_animal = Reptile(class_name, age, weight, *args)

    def get_animal(self):
        return self.create_animal


animal1 = AnimalFactory('bird', 36, 34, 5).create_animal
animal1.class_differences()
