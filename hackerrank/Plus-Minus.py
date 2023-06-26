n = int(input())
arr = list(map(int, input().split()))
positive = 0
negative = 0
zero = 0
for index in range(n):
    if arr[index] > 0:
        positive = positive + 1
    elif arr[index] == 0:
        zero = zero + 1
    else:
        negative = negative + 1
print(positive / n)
print(negative / n)
print(zero / n)