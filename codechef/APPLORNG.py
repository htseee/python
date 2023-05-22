n = int(input())
x1, x2 = map(int, input().split())
if x1 + x2 <= n:
	print("YES")
else:
	print("NO")