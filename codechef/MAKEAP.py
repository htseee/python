# cook your dish here
t = int(input())
for x in range(t):
    A, C = map(int, input().split())
    B = C - A
    if B % 2 == 0:
        print(A + B // 2)
    else:
        print(-1)