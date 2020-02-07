num = 2
simple_num = [num]
sum = 2


while len(simple_num) != 400:
    i = 0
    while i <= len(simple_num):
        if num%simple_num[i] != 0:
            if i == len(simple_num)-1:
                simple_num.append(num)
                sum+=num
            i+=1
        else:
            break
    num +=1

print(sum)
