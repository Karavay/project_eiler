number = 600851475143
biggest_divisor = 0
i = 2

while i <= number:
    if number%i == 0:
        number /=i
        biggest_divisor = i
        i = 2
    else:
        i += 1 

print("The biggest divisor is " + str(biggest_divisor))
