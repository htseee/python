t = int(input())
for x in range(t):
    A, B, C, D = map(int, input().split())
    if A - C > B - D:
        print("Second")
    elif A - C == B - D:
        print("Any")
    else:
        print("First")