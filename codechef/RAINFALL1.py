t = int(input())
for x in range(t):
    X = int(input())
    if X < 3:
        print("LIGHT")
    elif X >= 3 and X < 7:
        print("MODERATE")
    else:
        print("HEAVY")