t = int(input())
for x in range(t):
    X, Y, Z = map(int, input().split())
    if X > Y and X > Z:
        print("Setter")
    elif Y > Z:
        print("Tester")
    else:
        print("Editorialist")