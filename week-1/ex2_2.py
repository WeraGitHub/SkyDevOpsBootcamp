# Assign input value to a variable var
var = input("Please enter a value: ")

# print our variable as upper case
print(var.upper())

# print the number of characters in our variable
print(len(var))

# print out whether our variable is numeric
print(var.isdecimal())
print(var.isnumeric())

# check for numeric value in our variable
# first, declare a bool with value False
has_numeric = False
# iterate through each character in our variable
for char in var:
    # check if this character is a digit
    if char.isdigit():
        # if it is a digit then change the value of our boolean variable to True
        has_numeric = True
        # break
        break

# print out whether our variable has any numeric characters
print(has_numeric)
