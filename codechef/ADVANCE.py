t = int(input())
for x in range(t):
    X, Y = map(int, input().split())
    if Y >= X and Y <= X + 200:
        print("YES")
    else:
        print("NO")