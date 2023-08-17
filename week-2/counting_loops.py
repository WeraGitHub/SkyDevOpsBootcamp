# Alex and Weronika

# counting for loop, starting with 0 and ending with 4
for number in range(5):
    # print the number
    print(number)

# print empty line
print()

# counting for loop, starting at 2 and ending with 11, step of 3
for number in range(2, 13, 3):
    # print the number
    print(number)

# print empty line
print()

# create a list of names (strings)
names = ['Dom', 'Weronika', 'Nihal', 'Alex']
# another counting for loop
for i in range(0, len(names)):
    print(names[i])

# print empty line
print()

# create a list of numbers
numbers = [1, 2, 3, 4]

# classic for loop
for n in numbers:
    print(n)

# print empty line
print()

# counting for loop
for index, n in enumerate(numbers):
    print(index, n)
    numbers[index] += 5

print(numbers)
