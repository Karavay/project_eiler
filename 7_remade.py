import numpy as np

boolean_arr = [True]*1000
int_arr = []
i = 2
while i < len(boolean_arr) + 2:
    int_arr.append(i)
    j = 2
    while j <= np.sqrt(i):
            if i%j == 0:
                boolean_arr[i-2] = False
                break
            else:
                j += 1
    i += 1

print(int_arr)
print(boolean_arr)

# count = 0
#
# for i in boolean_arr:
#     if i == True:
#         count += 1
#
# print(count)
# AMOUNT OF SIMPLE NUMS

temp = len(boolean_arr) - 1

while temp > 0:
    if boolean_arr[temp] == True:
        print("the biggest simple number is {num}".format(num=temp+2))
        break

    temp -= 1
