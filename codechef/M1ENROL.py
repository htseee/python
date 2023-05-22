t = int(input())
for x in range(t):
	n, m = map(int, input().split())
	s = m - n
	if s > 0:
		print(s)
	else:
		print(0)