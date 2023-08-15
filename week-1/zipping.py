# Alex and Weronika

# create list with strings
farms = ['Home Farm', 'Muckworthy', 'Scales End', 'Brown Rigg']

# assign a list of integer numbers to a variable squirls
squirls = [42, 12, 2, 0]

# assign a list of integer numbers to a variable rabbits
rabbits = [395, 68, 57, 32]

# assign a list of integer numbers to a variable moles
moles = [12, 8, 0, 29]

# ZIP through other lists, access items in all the lists at the same time
for f, s, r, m in zip(farms, squirls, rabbits, moles):
    # output a string to the console, where f is an item from the farms list, s from the squirls and so on
    print('Total for', f, ':', s +r +m)

useless_rabbit_dictionary = {}
for f, r in zip(farms, rabbits):
    useless_rabbit_dictionary[f] = r

print(useless_rabbit_dictionary)
