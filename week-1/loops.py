# Alex and Weronika

# ///////////////////// while loops /////////////////////////////////////
# declare two integer variables
i = 1
j = 120

# while loop to increase i by doubling it, until i is >= 42
while i < 242:
    # multiply i by 2
    i = i * 2
    print(i)
    # if by any chance i is bigger than j now, exit the loop.
    if i > j: break
# once the loop is done execute else
else:
    print("Loop expired: ", i)

# output the final value to the console
print("Final value: ", i)


# ///////////////////// for loops /////////////////////////////////////
# create a list of names (strings)
names = ['Dom', 'Weronika', 'Nihal', 'Alex']
print(names)

# classic for each style loop
for name in names:
    print("Hello", name)

# ///////////////////// enumerate /////////////////////////////////////
# enumerate
for index, name in enumerate(names, start=1):
    print(index, name)
