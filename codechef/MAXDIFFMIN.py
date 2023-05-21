t = int(input())
for x in range(t):
    A, B, C = map(int, input().split())
    if A > B:
        A, B = B, A
    if A > C:
        A, C = C, A
    if B > C:
        B, C = C, B
    print(C - A)