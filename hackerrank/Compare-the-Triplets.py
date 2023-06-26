a = list(map(int, input().split()))
b = list(map(int, input().split()))
comparison = [0 for index in range(2)]
for index in range(3):
    if a[index] > b[index]:
        comparison[0] = comparison[0] + 1
    elif a[index] < b[index]:
        comparison[1] = comparison[1] + 1
print(comparison[0], comparison[1])