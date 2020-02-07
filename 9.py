import numpy

a = 1
b = 2
num = 1000

#1st solution
for a in range(1,1001):
    for b in range(2,1001):
        if 1000 - a - b == numpy.sqrt(a**2+b**2):#c = 1000 - a - b and c = numpy.sqrt(a**2+b**2)
            print("kek")
            break
    if 1000 - a - b == numpy.sqrt(a**2+b**2):
        c = numpy.sqrt(a**2+b**2)
        res = a*b*c
        print(res)
        break


#2nd solution
x = 1
y = 2

while 1000 - x - y != numpy.sqrt(x**2+y**2):
    y +=1
    if y == 1000:
        x+=1
        y = x+1

z = numpy.sqrt(x**2+y**2)

res = x*y*z
print(res)
