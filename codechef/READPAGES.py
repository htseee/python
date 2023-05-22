t = int(input())
for x in range(t):
    N, X, Y = map(int, input().split())
    if N <= X * Y:
        print("YES")
    else:
        print("NO")