from random import randint

ATTEMPTS = 10
LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(num)
count = ATTEMPTS

while count != 0:
    user_num = int(input("Осталось попыток: " + str(count) + ". Введите число: "))
    if user_num < num:
        print("Загаданное число больше")
    elif user_num > num:
        print("Загаданное число меньше")
    else:
        print("Поздравляем!!! Вы угадали число!!!")
        quit()
    count -= 1
else:
    print("К сожалению попытки закончились")
