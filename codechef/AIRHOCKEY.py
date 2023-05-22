def calc(x1, x2):
	ret = 0
	ret = min(7 - x1, 7 - x2)
	return ret
               	
if __name__ == "__main__":
	T = int(input())
	for t in range(T):
		x1, x2 = map(int, input().split())
		print(calc(x1, x2))