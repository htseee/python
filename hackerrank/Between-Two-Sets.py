n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
maxA = max(a)
minB = min(b)
count = 0
while maxA <= minB:
    setF = True
    for index in range(n):
        if maxA % a[index] != 0:
            setF = False
            break
    if setF:
        for index in range(m):
            if b[index] % maxA != 0:
                setF = False
                break
        if setF:
            count = count + 1
    maxA = maxA + 1
print(count)
