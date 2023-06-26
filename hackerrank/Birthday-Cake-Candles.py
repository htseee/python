n = int(input())
candles = list(map(int, input().split()))
tallest = 0
sum = 0
for index in range(n):
    if candles[index] > tallest:
        tallest = candles[index]
for index in range(n):
    if candles[index] == tallest:
        sum = sum + 1
print(sum)