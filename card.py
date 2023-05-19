t = int(input())
for x in range(t):
    N, X = map(int, input().split())
    print(min(X, N - X))