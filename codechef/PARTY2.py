def calc(n, x1, x2):
	ret = "NO"
	if n <= (x2 // x1):
		ret = "YES"
	return ret

if __name__ == "__main__":
	T = int(input())
	for t in range(T):
		n, x1, x2 = map(int, input().split())
		print(calc(n, x1, x2))