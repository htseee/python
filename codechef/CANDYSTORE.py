t = int(input())
for x in range(t):
    X, Y = map(int, input().split())
    S = min(X, Y)
    if Y - X > 0:
        S = S + 2 * (Y - X)
    print(S)