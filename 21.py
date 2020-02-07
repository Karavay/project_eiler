def f(num):
    a,b = 0,1
    while a<num:
        print(a,end=' ')
        a,b = b,a+b


f(10)
