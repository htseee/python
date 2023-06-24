num = list(map(int, input().split()))
sum = 0
minNum = 1000000000
maxNum = 0
for index in range(5):
    sum = sum + num[index]
    if minNum > num[index]:
        minNum = num[index]
    if maxNum < num[index]:
        maxNum = num[index]
print(sum - maxNum, sum - minNum)
