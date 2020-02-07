import math

def amountOfWays(a,b):
    amount = math.factorial(a+b)/(math.factorial(a)*math.factorial(b))
    return amount

print(amountOfWays(3,3))
