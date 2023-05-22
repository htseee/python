t = int(input())
for t in range(t):
    A, B, C = map(int, input().split())
    S = A
    person = "Alice"
    if A < B:
        S = B
        person = "Bob"
    if S < C:
        S = C
        person = "Charlie"
    print(person)    