

def find_largest_value(m):
	highest = m[0][0]
	for row in m:
		for cell in row:
			if cell > highest:
				highest = cell
	return highest




matrix = [[1, 2, 3], 
          [0, 5, 4], 
          [1, 6, 2]]

max_value = find_largest_value(matrix)
print(max_value)