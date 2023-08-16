
# create a binary file (single byte strings)
# file_handle = open('file_data.txt', 'wb')
# number_of_bytes = file_handle.write(b'This is a binary string\n')
# print(number_of_bytes)
#
# regular_string = "This is a sentence.\n"
# number_of_bytes = file_handle.write(regular_string.encode())
# print(number_of_bytes)

for line in open('file_data.txt', 'rb'):
    print(line.decode(), end='')
