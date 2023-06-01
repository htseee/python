# cook your dish here
import math

t = int(input())
for x in range(t):
    N, M = map(int, input().split())
    online_cost = round(N - 10 / 100 * N)
    if online_cost == M:
        print("EITHER")
    elif online_cost > M:
        print("DINING")
    else:
        print("ONLINE")