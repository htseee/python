n = int(input())
grades = []
for index in range(n):
    grades.append(int(input()))
for index in range(n):
    if grades[index] < 38:
        print(grades[index])
    else:
        if grades[index] % 5 == 0:
            print(grades[index])
        elif (grades[index] + 1) % 5 == 0:
            print(grades[index] + 1)
        elif (grades[index] + 2) % 5 == 0:
            print(grades[index] + 2)
        else:
            print(grades[index])