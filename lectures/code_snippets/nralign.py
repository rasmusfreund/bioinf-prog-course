from math import factorial

for n in range(1, 21):
    nr = factorial(2*n) / factorial(n)**2
    print(n, nr)
