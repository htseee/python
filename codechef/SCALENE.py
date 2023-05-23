t = int(input())
for x in range(t):
    A, B, C = map(int, input().split())
    if A != B and A != C and B != C:
        print("YES")
    else:
        print("NO")