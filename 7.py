simple_num = []
num = 2

while len(simple_num) != 10001:
    i = 0
    while i <= len(simple_num):
        if len(simple_num) != 0:
            if num%simple_num[i] != 0:
                if i == len(simple_num)-1:
                    simple_num.append(num)
                i+=1
            else:
                i = 0
                break
        else:
            simple_num.append(num)
    num +=1

print(simple_num[10000])
