t = int(input())
for x in range(t):
    X, Y = map(int, input().split())
    disposable = 100 * X
    cloth = 10 * Y
    if disposable > cloth or disposable == cloth:
        print("Cloth")
    else:
        print("Disposable")