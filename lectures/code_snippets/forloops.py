

matrix = [[1, 2, 3], 
          [0, 5, 4], 
          [1, 6, 2]]

largest = 0
nr_rows = len(matrix)
for i in range(nr_rows):
	nr_cols = len(matrix[i])
	for j in range(nr_cols):
		value = matrix[i][j]
		if value > largest:
			largest = value
print(largest)








































# result = []
# for i in range(len(matrix)):
# 	result.append(matrix[i][0])

# print(result)

# result = []
# for row in matrix:
# 	result.append(row[0])

# print(result)


# diagonal = []

# for i in range(len(matrix)):
# 	for j  in range(len(matrix[i])):
# 		if i == j:
# 			diagonal.append(matrix[i][j])

# print(diagonal)