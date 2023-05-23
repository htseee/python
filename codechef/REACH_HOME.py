t = int(input())
for x in range(t):
    X, Y = map(int, input().split())
    if 5 * X >= Y:
        print("YES")
    else:
        print("NO")