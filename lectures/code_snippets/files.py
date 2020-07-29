

from sys import argv

input_file_name = argv[1]
output_file_name = argv[2]

data_file = open(input_file_name, 'r')

output_file = open(output_file_name, 'w')

for line in data_file:
    numbers = line.split()
    number1 = int(numbers[0])
    number2 = int(numbers[1])
    result = number1 + number2
    print(result, file=output_file)

data_file.close()
output_file.close()
