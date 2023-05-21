t = int(input())
for x in range(t):
    N, X, Y = map(int, input().split())
    if N < X + 2 * Y:
        print("NO")
    else:
        print("YES")