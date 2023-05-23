t = int(input())
for x in range(t):
    X, Y = map(int, input().split())
    if X > 0 and Y > 0 and X == Y:
        print("YES")
    else:
        print("NO")