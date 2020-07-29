
def fibo(n):    
	if n <= 2:
		return 1
	return fibo(n-1) + fibo(n-2)

def fibo(n):    
    if n <= 2:
        return 1
    else:
        a, b = 1, 1
        for i in range(n-2):
            c = a + b
            a, b = b, c
        return c

print(fibo(305))













# def fibo(n):    
#     if n <= 2:
#         return 1
#     return fibo(n-1) + fibo(n-2)

# print(fibo(7))