t = int(input())
for x in range(t):
    X, Y = map(int, input().split())
    if X > Y:
        print(X - Y)
    else:
        print(0)