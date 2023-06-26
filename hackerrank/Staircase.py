n = int(input())
for index in range(n):
    print(' ' * (n - index - 1), '#' * (index + 1), sep='')