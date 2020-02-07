def eiler6(range):
    num1 = 0
    num2 = 0
    i = 0
    while i <= range:
        num1 += i**2
        num2 += i
        i += 1

    num2 **= 2

    return num2 - num1

print(eiler6(100))
