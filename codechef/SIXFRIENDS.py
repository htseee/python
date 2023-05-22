t = int(input())
for x in range(t):
    X, Y = map(int, input().split())
    print(min(3 * X, 2 * Y))