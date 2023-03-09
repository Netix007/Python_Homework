a = 0
while a > 100000 or a <= 0:
    a = int(input("Введите целое число от 1 до 100000: "))
for i in range(2, a):
    if a % i == 0:
        break
else:
    print("Число", a, "- простое")
    quit()
print("Число", a, "- составное")