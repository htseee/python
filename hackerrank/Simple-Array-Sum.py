n = int(input())
ar = list(map(int, input().split()))
sum = 0
for index in range(n):
    sum = sum + ar[index]
print(sum)