X, Y = map(float, input().split())
X = int(X)
if X % 5 == 0 and X + 0.5 <= Y:
    print(Y - X - 0.5)
else:
    print(Y)