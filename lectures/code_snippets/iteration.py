

list_of_lists = []
for i in range(3):
	lst = []
	for j in range(4):
		lst.append(i*j)
	list_of_lists.append(lst)

print(list_of_lists)