# create two string variables, one for my first name and second for my surname
first_name = "Weronika"
last_name = "Limberger"

# output my variables by using print function
print("My name is " + first_name + " " + last_name)

# create a list and use the previous variables as list items
name_list = [first_name, last_name]
# display the list
print(name_list)
# alternative way - using casting
print("List: " + str(name_list))

# create dictionary with keys: first and last, where values are our original variables
name_dictionary = {"first": first_name, "last": last_name}
# output our dictionary to the console
print(name_dictionary)
