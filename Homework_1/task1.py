print("Введите стороны треугольника")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a >= b + c or b >= a + c or c >= a + b:
    print("Треугольника с такими сторонами не существует")
elif a == b == c:
    print("Треугольник равносторонний")
elif a == b or a == c or b == c:
    print("Треугольник равнобедренный")
else:
    print("Треугольник разносторонний")