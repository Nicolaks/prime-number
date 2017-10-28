

def is_prime(n):
	for i in range(2, n):
		if n%i == 0:
			return False
	return True


n = int(input("What number should I go up to ? "))

for p in range(2, n+1):
	if is_prime(p):
		print(p)
