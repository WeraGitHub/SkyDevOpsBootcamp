euro = "\u20ac"
print(euro + "2.99")
print("\N{euro sign}" + "5.99")

print('one', end="\n")   # new line is a default behaviour
print('two', end="----")
print("three")
print("four", "five", "six", sep=" ! ")  # separator, default one is a space


# Alex and Weronika

# declare the text variable with a string in it
text = 'hello world'  # string with single quotes

# print how many times character o is in our text string
print(text.count('o'))

# check if our text string starts with substring 'hell'
if text.startswith('hell'):
    print("It's hell in there!")

# check if our text string has all the characters alphabetic
if text.isalpha():
    # if it's true print this:
    print('string is all alpha')
else:
    # otherwise
    print('not all characters in our string are alphabetic')

# declare the text2 variable with a string in it
text2 = "helloworld"  # string with double quotes
if text2.isalpha():
    print('string2 is all alpha')  # this time there are no spaces in our string

# reassign new value to our text variable
text = ' \t\r\n'  # \t is tab, \r is carriage return, \n is new line
# check if our string variable is all whitespace
if text.isspace():
    print('string \t \t is \t \t whitespace')
