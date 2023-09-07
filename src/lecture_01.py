# x=4
# for n in range(x-1,-1,-1):
#     print(n)
# for n in range(1,x+1):
#         print(n)
# for n in range(-1,-x-1,-1):
#         print(n)
# i = 1
# for i in range(3):
#     for j in range (4):
#         print(i, j)
# data_file = open('/home/hans/uni/autumn-23/comp_thinking/data.txt', 'r')

# file_content = data_file.read()
# print(file_content)
# for line in data_file:
#     print(line)

# data_file = open('/home/hans/uni/autumn-23/comp_thinking/output.txt', 'w')

# print('First line', file = data_file)
# print('Second line', file=data_file)
# input_file = open('/home/hans/uni/autumn-23/comp_thinking/data.txt', 'r')
# output_file = open('/home/hans/uni/autumn-23/comp_thinking/result.txt', 'w')
# file_content= input_file.read()
# output_file.write(file_content)
from sys import argv
print(argv)
input_file_name = argv[1]
output_file_name = argv[2]
print(input_file_name)
print(output_file_name)

