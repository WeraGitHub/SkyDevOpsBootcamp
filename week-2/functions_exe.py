# Kamil, Nathan and Weronika

# declare an empty list
countries = []

# iterate over every line in country.txt file
for line in open('country.txt'):
    # and splits each item in the line
    countries.append(line.split(','))

# sorts the countries list ascending order alphabetically
countries.sort()

# sorting the countries list by second element (population)
countries.sort(key=lambda c: int(c[1]))

# sorting the list in the descending order
countries.sort(reverse=True)

# iterating through countries list
for line in countries:
    # print a string made out of items in a line in a list of countries, joined by  a come
    print(','.join(line), end='')
