t = int(input())
for x in range(t):
    A = int(input())
    S = A % 3
    if S == 0:
        print(0)
    else:
        print(3 - S)