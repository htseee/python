t = int(input())
for x in range(t):
    A, B = map(int, input().split())
    if (A + B) % 2 == 0:
        print("YES")
    else:
        print("NO")