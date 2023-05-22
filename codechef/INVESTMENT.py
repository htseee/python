T = int(input())
for t in range(T):
	n, m = map(int, input().split())
	if n >= (m << 1):
		print("YES")
	else:
		print("NO")