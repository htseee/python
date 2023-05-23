import math

t = int(input())
for x in range(t):
    N, M, K = map(int, input().split())
    if math.ceil(N / K) <= M:
        print("Yes")
    else:
        print("No")