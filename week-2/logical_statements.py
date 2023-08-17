# Alex and Weronika

# assign integer values to variables a - e
a = 10
b = 5
c = 2
d = 1
e = 8

# check if a is bigger than b
if a > b :  # a > b evaluates to True
    # then print this:
    print("a is bigger than b")
else:
    # otherwise print this:
    print("a is NOT bigger than b")

# check if a is bigger than b AND False, so we have True AND False
if a > b and False:  # evaluates to True and False, which ends up as False
    # then print this:
    print("both statements are true")
else:
    # otherwise print this:
    print("at least one of them is false")

# check if a is bigger than b AND False, so we have True AND NOT False
if a > b and not False:  # evaluates to True and True, which ends up as True
    print("both statements are true")
else:
    print("at least one of them is false")


if True or (not True and True):
    print("Trueee")
else:
    print("Falsssee")

if True or not True and True:
    print("Trueee")
else:
    print("Falsssee")

if a > b and not a > b:  # a > b evaluates to True and False
    # then print this:
    print("both statements are true")
else:
    # otherwise print this:
    print("at least one of them is false")

if a > b or not a > b:  # a > b evaluates to True and False
    # then print this:
    print("at least one statement is true")
else:
    # otherwise print this:
    print("both statements are false")

print()
print()


if (a > b or not a > b) and (a > b and not a > b):  # a > b evaluates to True
    # then print this:
    print("It all evaluates to TRUE")
else:
    # otherwise print this:
    print("FALSE")


if a > b or not a > b and a > b and not a > b:  # a > b evaluates to True
    # then print this:
    print("It all evaluates to TRUE")
else:
    # otherwise print this:
    print("FALSE")
