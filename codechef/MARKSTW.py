def calc(x1, x2):
	ret = "NO"
	if x1 >= (x2 << 1):
		ret = "YES"
	return ret

if __name__ == "__main__":
	x1, x2 = map(int, input().split())
	print(calc(x1, x2))