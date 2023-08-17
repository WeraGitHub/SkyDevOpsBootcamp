# import the say_hello funtion from different python module
from greet_functions import say_hello

# use build-in function print(), inside it call our function, while passing our names as arguments
print(say_hello("Nathan", "Weronika"))

a = 42
print(a)
del a  #  del is a statement
# print(a)
# printing deleted value will cause an error

print(locals())
print(type(locals()))