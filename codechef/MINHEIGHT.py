t = int(input())
for x in range(t):
    X, H = map(int, input().split())
    if X >= H:
        print("YES")
    else:
        print("NO")