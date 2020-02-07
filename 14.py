#n - n/2 chet
#n - n*3+1 nechet


def get_kolatz(num,amount):
    if num == 1:
        return amount
    elif num%2 == 0:
        return get_kolatz(num//2,amount+1)
    else:
        return get_kolatz(num*3+1,amount+1)

q = 0
w = 0
for i in range(13,1000000):
    c = get_kolatz(i,1)
    if c>w:
        q,w=i,c



print(q,w)
