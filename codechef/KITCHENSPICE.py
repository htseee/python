t = int(input())
for x in range(t):
    X = int(input())
    if X < 4:
        print("MILD")
    elif X >= 4 and X < 7:
        print("MEDIUM")
    else:
        print("HOT")