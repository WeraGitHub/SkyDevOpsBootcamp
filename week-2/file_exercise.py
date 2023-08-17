# Alex and Weronika

# open country.txt file in a read and binary mode
country_file_handler = open('country.txt', 'rb')

# declare an empty dictionary
index = {}

while True:
    # read one line from our file
    line = country_file_handler.readline()
    # break out of the loop if no line to read or if it is empty
    if not line: break
    # split our line into a list
    fields = line.decode().split(',')
    # Key: fields[0] (i.e. country name)
    # Value: position of pointer at beginning of corresponding line
    index[fields[0]] = country_file_handler.tell() - len(line)

print(index)
# ask user to input a value in the terminal
key = input('Enter a country: ')
# find the line of code which first item matches the string that was entered by the user
country_file_handler.seek(index[key])

# print the line the pointer is at
print(country_file_handler.readline().decode(), end="")


while True:
    # read one line from our file
    line = country_file_handler.readline()
    # break out of the loop if no line to read or if it is empty
    if not line: break
    # split our line into a list
    fields = line.decode().split(',')
    # Key: fields[0] (i.e. country name)
    # Value: position of pointer at beginning of corresponding line
    index[fields[0]] = country_file_handler.tell() - len(line)