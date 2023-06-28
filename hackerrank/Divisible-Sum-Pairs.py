n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = sum(1 for index in range(n) for indexA in range(index + 1, n) if (arr[index] + arr[indexA]) % k == 0)
# for index in range(n):
#     for indexA in range(index + 1, n):
#         if (arr[index] + arr[indexA]) % k == 0:
#             count = count + 1
print(count)