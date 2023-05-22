t = int(input())
for x in range(t):
    N, K = map(int, input().split())
    if N < K:
        print("YES")
    else:
        print("NO")