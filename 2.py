sum = 0
i = 0 #1st num
j = 1 #2nd num
k = j + i # sum of 1st and 2nd
while i <= 4000000:
    if i%2==0:
        sum += i
    i = j
    j = k
    k = i + j

print(sum)
