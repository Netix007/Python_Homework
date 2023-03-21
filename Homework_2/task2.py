from fractions import Fraction


def fraction_reduction(x: str):
    result = x
    a = x.split("/")
    max_num = int(a[0])+1
    for i in range(2, max_num):
        if int(a[0]) % i == 0 and int(a[1]) % i == 0:
            a[0] = str(int(a[0]) // i)
            a[1] = str(int(a[1]) // i)
            result = fraction_reduction(a[0] + "/" + a[1])
            break
    return result


def check_int(x: str):
    b = x.split("/")
    if int(b[0]) == int(b[1]):
        return "1"
    else:
        return x


def sum_of_fractions(num3: str, num4: str):
    a = num3.split("/")
    b = num4.split("/")
    if int(a[1]) == int(b[1]):
        c = int(a[0]) + int(b[0])
        result = f'{c}/{a[1]}'
    else:
        c = int(a[0])*int(b[1]) + int(b[0])*int(a[1])
        result = f'{c}/{int(a[1])*int(b[1])}'
    result = fraction_reduction(result)
    return check_int(result)


def multiplication_of_fractions(num3: str, num4: str):
    a = num3.split("/")
    b = num4.split("/")
    result = f'{int(a[0])*int(b[0])}/{int(a[1])*int(b[1])}'
    return result


num1 = str(input("Input first number x = "))
num2 = str(input("Input second number y = "))
print(f'The result of the program: x + y = {sum_of_fractions(num1, num2)}')
print(f'The result of the integrated modul "fractions": x + y = {Fraction(num1)+Fraction(num2)}')
print(f'The result of the program: x * y = {multiplication_of_fractions(num1, num2)}')
print(f'The result of the integrated modul "fractions": x * y = {Fraction(num1)*Fraction(num2)}')
