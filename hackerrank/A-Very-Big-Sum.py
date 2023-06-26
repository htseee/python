n = int(input())
arr = list(map(int, input().split()))
sum = 0
for index in range(n):
    sum = sum + arr[index]
print(sum)