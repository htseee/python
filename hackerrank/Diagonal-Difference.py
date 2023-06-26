n = int(input())
arr = []
for index in range(n):
    arr.append(list(map(int, input().split())))
sumDiagonal = 0
sumDiagonalSecondary = 0
for index in range(n):
    sumDiagonal = sumDiagonal + arr[index][index]
    sumDiagonalSecondary = sumDiagonalSecondary + arr[index][n - index - 1]
print(abs(sumDiagonal - sumDiagonalSecondary))