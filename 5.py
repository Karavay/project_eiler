num = 0
x = 0

while True:
    i = 1

    while i <= 20:
        if num%i == 0:
            if i == 20:
                x = num
                break
            i+=1
        else:
            break
    if x != 0:
        print(x)
        break

    num+=1
