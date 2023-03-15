a = int(input("Input number: "))
temp = a
if a == 0:
    result = "0"
else:
    result = ""
    while temp != 0:
        remainder = temp % 16
        if remainder == 10:
            result = "a"+result
        elif remainder == 11:
            result = "b"+result
        elif remainder == 12:
            result = "c"+result
        elif remainder == 13:
            result = "d"+result
        elif remainder == 14:
            result = "e"+result
        elif remainder == 15:
            result = "f" + result
        else:
            result = str(remainder) + result
        temp = temp // 16
print("The result of the program:", result)
print("The result of the hex() function:", hex(a)[2:])
