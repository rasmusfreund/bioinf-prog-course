
def square(number):
	result = number**2
	return result

def sum_of_squares(x, y, z):
	sq1 = square(x)
	sq2 = square(y)
	sq3 = square(z)
	return sq1 + sq2 + sq3

x = sum_of_squares(4, -2, 3)
print(x)