t = int(input())
for x in range(t):
    X, Y, Z = map(int, input().split())
    print((5 * X + 10 * Y) // Z)