t = int(input())
for x in range(t):
    X, Y = map(int, input().split())
    if X > Y:
        print("SECOND")
    elif X == Y:
        print("ANY")
    else:
        print("FIRST")