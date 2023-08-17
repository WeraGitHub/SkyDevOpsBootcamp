
file_handle = open('file_hobbies.txt')

# buffer = file_handle.read(42)
# print(buffer)
#
# buffer2 = file_handle.read(3)
# print(buffer2)
#
# line = file_handle.readline()
# print(line)
#
# for line in open('file_hobbies.txt'):
#     print(line, end="")
#
# # slurping what do you call reading whole file in one go
# lines = open('file_hobbies.txt').read()
# print(type(lines))
# print(lines)
#
# list_lines = open('file_hobbies.txt').read().splitlines()
# print(type(list_lines))
# print(list_lines)

with open('file_hobbies.txt', 'r') as file_handle:
    for line in file_handle:
        print(line, end='')

