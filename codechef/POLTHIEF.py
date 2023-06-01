t = int(input())
for x in range(t):
    X, Y = map(int, input().split())
    if X > Y:
        X, Y = Y, X
    time = 0
    while Y > X:
        l = Y - X
        current_time = l // 2
        if l % 2 == 1:
            current_time = current_time + 1
        Y = Y + current_time
        X = X + 2 * current_time
        time = time + current_time
    print(time)