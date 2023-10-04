
def fibo(n):    
    if n <= 2:
        return 1
    else:
        a, b = 1, 1
        for dummy in range(n-2):
            c = a + b
            a, b = b, c
        return c

print(fibo(30))
print(fibo(40))        