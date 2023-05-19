# Click on 'Next' once you are ready to proceed.
t = int(input())
for x in range(t):
    A, C = map(int, input().split())
    S = A + C
    if S % 2 == 0:
        print(S // 2)
    else:
        print(-1)