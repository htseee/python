s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))
sumApples = 0
sumOranges = 0
for index in range(m):
    apples[index] = apples[index] + a
for index in range(n):
    oranges[index] = oranges[index] + b
for index in range(m):
    if apples[index] >= s and apples[index] <= t:
        sumApples = sumApples + 1
for index in range(n):
    if oranges[index] >= s and oranges[index] <= t:
        sumOranges = sumOranges + 1
print(sumApples)
print(sumOranges)