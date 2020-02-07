#100*101 100*102 с проверкой на полиморфность если да то в массив

massiv_polinomialnix = []
a = 100
b = 100

while a < 1000 and b < 1000:

    check_array = []
    num = a * b

    while num != 0 :
        check_array.append(num%10)
        num //= 10

    num = a * b
    i = 0
    j = len(check_array)-1
    while i <= j:
        if check_array[i] == check_array[j]:
            if i+1 >= j-1:
                massiv_polinomialnix.append(num)
                break#нашел ошибку!!!
            i+=1
            j-=1
        else:
            break
    #итерация
    if b < 999:
        b+=1
    else:
        a += 1
        b = a

print(sorted(massiv_polinomialnix))
print("nashe samoe bolshoe chislo - " + str(max(massiv_polinomialnix)))
