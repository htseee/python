t = int(input())
for x in range(t):
    X, Y = map(int, input().split())
    if X / 10 > Y:
        print("YES")
    else:
        print("NO")