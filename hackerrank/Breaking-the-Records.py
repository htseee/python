n = int(input())
score = list(map(int, input().split()))
mostPoint = 0
leastPoint = 0
minScore = score[0]
maxScore = score[0]
for index in range(n):
    if score[index] > minScore:
        minScore = score[index]
        mostPoint = mostPoint + 1
    if score[index] < maxScore:
        maxScore = score[index]
        leastPoint = leastPoint + 1
print(mostPoint, leastPoint)