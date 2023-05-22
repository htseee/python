t = int(input())
for x in range(t):
	X, Y = map(int, input().split())
	if 3 * X <= Y:
		print("YES")
	else:
		print("NO")