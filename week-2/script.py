#!/usr/bin/env python3
# the above is used to specify the path to the Python interpreter that should be used to run a Python script on the first line

# is a comment - title
# Example Python script

# importing python module called sys
import sys

# count number of arguments passed to the command line using len() funtion
number_of_sys_arguments = len(sys.argv)  # sys.argv is arguments passed to the command line

# check if the number of arguments is more than one
if number_of_sys_arguments > 1:
    # if it's true then use print() function to display the text in the terminal
    print('Too many args')
# otherwise
else:
    # create a variable and assign a string to it
    where = 'World'
    # then use print() function to display the text in the terminal
    print("Hello", where)

# print this goodbye message with first argument (this python file)
print('Goodbye from ' + sys.argv[0])
