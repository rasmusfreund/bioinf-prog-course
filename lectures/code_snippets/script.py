
from sys import argv

input_file_name = argv[1]
output_file_name = argv[2]

data_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')

for line in data_file:
    fields = line.split()
    n1 = int(fields[0])
    n2 = int(fields[1])
    print(n1 + n2, file=output_file)

data_file.close()

