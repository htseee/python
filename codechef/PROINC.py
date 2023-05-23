t = int(input())
for x in range(t):
    X, Y = map(int, input().split())
    S = round(0.1 * X)
    print(Y + S)