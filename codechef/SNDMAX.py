t = int(input())
for x in range(t):
    X1, X2, X3 = map(int, input().split())
    if X1 > X2:
        X1, X2 = X2, X1
    if X1 > X3:
        X1, X3 = X3, X1
    if X2 > X3:
        X2, X3 = X3, X2        
    print(X2)