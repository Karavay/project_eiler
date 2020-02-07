import numpy as np
i = 1#итератор ,принимающий значения треугольного числа
j = 2#увеличитель треугольного числа)))

while(True):
    arr = []#массив делителей треугольного числа
    k = 1#первый делитель
    while (k<=np.sqrt(i)):
        if i%k == 0:
            arr.append(k)
            q = i/k
            if q > np.sqrt(i):
                arr.append(q)
        k+=1

    if(len(arr)>=500):
        print("First triange num with 500 or more divisors is " + str(i))
        print(arr)
        print("amount of divisors :"+str(len(arr))
        break

    else:
        i+=j
        j+=1
