t = int(input())
for x in range(t):
    A, B, C = map(int, input().split())
    if A == B + C or B == A + C or C == A + B:
        print("YES")
    else:
        print("NO")