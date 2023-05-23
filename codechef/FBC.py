t = int(input())
for x in range(t):
    K, X = map(int, input().split())
    if K < X:
        print(0)
    else:
        print(K - X)