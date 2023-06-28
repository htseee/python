from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
c = Counter(arr)
maxFrequence = max(c.values())
type = [key for key, value in c.items() if value == maxFrequence]
print(min(type))
# c = [0 for type in range(5 + 1)]
# for index in range(n):
#     c[arr[index]] = c[arr[index]] + 1
# maxFrequence = 0
# typeFrequence = 0
# for type in range(5 + 1):
#     if c[type] != 0 and c[type] > maxFrequence:
#         maxFrequence = c[type]
#         typeFrequence = type
# print(typeFrequence)