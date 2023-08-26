from datetime import timedelta

li = [1,2,3,4,5]

max_1 = -999999999
max_2 = -999999999

for i in range(len(li)):
    if li[i] > max_1:
        max_1 = li[i]

for j in range(len(li)):
    if li[j] < max_1 and li[j] > max_2:
        max_2 = li[j]

print(max_2)