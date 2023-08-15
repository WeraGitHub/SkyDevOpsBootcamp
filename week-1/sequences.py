# Alex and Weronika

# create a list with four integer values and assign it to a variable mylist
mylist = [0, 1, 2, 3]

# check if mylist is truthy
if mylist:
    print("mylist is True")
else:
    print("mylist is False")

# create an empty list
mylist2 = []
# check if mylist2 is truthy
if mylist2:
    print("mylist2 is True")
else:
    print("mylist2 is False")

# create a  list full of Falsy items
mylist3 = [None, 0, False, []]
# check if mylist3 is truthy
if mylist3:
    print("mylist3 is True")
else:
    print("mylist3 is False")

if all(mylist3):
    print("All the list items are Truthy")
else:
    print("At least one of the items in my list 3 is False")

if all(mylist3):
    print("At least one of the items in my list 3 is False")
else:
    print("All the list items are Truthy")

if any(mylist3):
    print("At lease one item is True")
else:
    print("Every item in this list is False")

