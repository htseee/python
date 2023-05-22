t = int(input())
for x in range(t):
	X, P, Q = map(int, input().split())
	if P > Q:
		print(X * (P - Q))
	else:
		print(0)