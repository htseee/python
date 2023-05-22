t = int(input())
for x in range(t):
    N, M, X = map(int, input().split())
    print(2 * (N + M) * X)