
s = 'ABCDEFGHIJKLMNOPQRST'
k = 5

for i in range(len(s)-k+1):
    print(s[i:i+k], s[i+k+4:])
