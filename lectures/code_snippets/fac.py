
def fakultet(n):
	if n == 1:
		return 1
	return n * fakultet(n-1)

result = fakultet(100)
print(result)