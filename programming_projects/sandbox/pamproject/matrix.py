

matrix = [[0.8, 0.1, 0.1], 
          [0.1, 0.8, 0.1], 
          [0.1, 0.1, 0.8]]

p = 3

def mat_pow(m, power):
    other = m
    for dummy in range(power-1):
        prod = []
        for i in range(len(m)):
            row = []
            for j in range(len(m)):
                val = 0
                for k in range(len(m)):
                    val += other[k][i] * m[j][k]
                row.append(val)
            prod.append(row)
        other = prod[:]
    return prod

print(mat_pow(matrix, p))

def mat_pow(m, power):
    other = m
    n = len(m)
    for dummy in range(power-1):
        prod = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(sum(other[k][i] * m[j][k] for k in range(n)))
            prod.append(row)
        other = prod[:]
    return prod

print(mat_pow(matrix, p))

def mat_pow(m, power):
    other = m[:]
    n = len(m)
    for dummy in range(power-1):
        other = [[sum(other[k][i] * m[j][k] for k in range(n)) for j in range(n)] for i in range(n)]
    return other

print(mat_pow(matrix, p))

