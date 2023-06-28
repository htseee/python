n = int(input())
s = list(map(int, input().split()))
d, m = map(int, input().split())
c = [sum(s[index:index + m]) for index in range(n - m + 1)]
# for index in range(n - m + 1):
#     if sum(s[index:index + m]) == d:
#         count = count + 1
print(c.count(d))