
def factorial(x):    
	result = 1
	for n in range(1, x+1):
		result = result * n
	return result

print(factorial(10))
#print(factorial(1000))	