if __name__ == "__main__":
	T = int(input())
	for t in range(T):
		x1, x2 = map(int, input().split())		
		if x1 > x2:
			print("YES")
		else:
			print("NO")